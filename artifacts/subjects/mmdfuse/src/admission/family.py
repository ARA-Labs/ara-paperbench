"""Registered finite T-MF1 families and deployer-owned scientific decisions."""
from __future__ import annotations

from aratest.generative import Perturbation
from aratest.research import (
    AdjudicatorView,
    ControlRequirement,
    DesignFactor,
    DesignMatrix,
    Estimand,
    ExperimentProposal,
    FamilyMeasurement,
    ImplementationFamily,
    ProposalBudget,
    ProposerView,
    ResearchState,
    ScopeAssessment,
    StatePool,
    VerdictContext,
)
from aratest.research.controls import (
    ControlComparison,
    ControlComparisonInputs,
    ControlEvaluationPlan,
    ControlRuleOutcome,
    RegisteredObservationSelector,
)
from aratest.traits import VerdictOutcome

from .protocol import control_passes, map_request

CLAIM_ID: str = 'C12'
RULE_ID: str = 'mmdfuse.mean-treatment.v1'
TARGET_STATEMENT: str = ('T-MF1 evaluates robustness of the author-reported mixture-cell rejection proportion '
                         'under the registered released-code seed and within-group row-order interventions.')


def make_proposal(generator: int, manifests: tuple[str, ...] = ()) -> ExperimentProposal:
    if generator == 1:
        cells: tuple[Perturbation, ...] = (
            (('jax_seed', 42), ('label_permutation', 0)),
            (('jax_seed', 42), ('label_permutation', 1)),
            (('jax_seed', 43), ('label_permutation', 0)),
        )
        factors = (DesignFactor(name='jax_seed', role='nuisance', levels=(42, 43)),
                   DesignFactor(name='label_permutation', role='intervention', levels=(0, 1)))
        treatment_indices = (0, 2)
    elif generator == 2 and len(manifests) == 2:
        cells = tuple(sorted(((('label_permutation', 0), ('row_permutation', digest))) for digest in manifests))
        control: Perturbation = (('label_permutation', 1), ('row_permutation', manifests[0]))
        cells = (*cells, control)
        factors = (DesignFactor(name='label_permutation', role='intervention', levels=(0, 1)),
                   DesignFactor(name='row_permutation', role='nuisance', levels=tuple(sorted(manifests))))
        treatment_indices = (0, 1)
    else:
        raise ValueError('unsupported registered family')
    selectors = tuple(RegisteredObservationSelector(cell=cell, repetition=0) for cell in cells)
    treatment = tuple(sorted((selectors[i] for i in treatment_indices), key=lambda x: x.model_dump_json()))
    reference = selectors[0] if generator == 1 else next(s for s in selectors if dict(s.cell)['row_permutation'] == manifests[0] and dict(s.cell)['label_permutation'] == 0)
    negative = next(s for s in selectors if dict(s.cell)['label_permutation'] == 1)
    return ExperimentProposal(
        proposal_id=f'T-MF1-G{generator}', proposer_id='mmdfuse.registered-family.v1',
        claim_id=CLAIM_ID, family='setup_perturbation' if generator == 1 else 'resampling',
        intent='robustness', mode='confirmatory_closed', proposed_relation='scope_preserving',
        estimand=Estimand(population='registered finite mixture cells',
                         intervention='parent JAX seed' if generator == 1 else 'within-group row order',
                         comparator='released-code reference cell', outcome='rejection_proportion',
                         aggregation='mean treatment rejection proportion'),
        design=DesignMatrix(factors=factors, randomization='none', repetitions=1, cells=cells),
        controls=(ControlRequirement(control_id='labels', kind='negative',
                                    diagnostic_target='separation signal',
                                    comparability_proof='same drawn pair and test key; pooled rows relabelled'),),
        control_evaluation=ControlEvaluationPlan(treatment=treatment, comparisons=(
            ControlComparison(control_id='labels', rule_id='mmdfuse.label-degradation.v1',
                              reference=(reference,), control=(negative,)),)),
        decision_rule_id=RULE_ID, needs_adaptation=False,
    )


class TargetScheduler:
    scheduler_id: str = 'mmdfuse.target-T-MF1.v1'

    def select(self, pool: StatePool) -> ResearchState | None:
        return next((s for s in pool.open_states() if s.claim_id == CLAIM_ID), None)


class RegisteredFamily:
    family_version: str = '1'

    def __init__(self, generator: int, manifests: tuple[str, ...] = ()) -> None:
        self.proposal = make_proposal(generator, manifests)
        self.family_id: ImplementationFamily = self.proposal.family

    def propose(self, state: ProposerView, budget: ProposalBudget) -> tuple[ExperimentProposal, ...]:
        if state.claim_id != CLAIM_ID or 'T-MF1' not in state.scope.claim_text or budget.max_cells < 3:
            return ()
        return (self.proposal,)


class MethodScopeAdjudicator:
    adjudicator_id: str = 'mmdfuse.released-protocol-scope.v1'
    adjudicator_version: str = '1'

    def __init__(self, generator: int, manifests: tuple[str, ...] = ()) -> None:
        self.expected = make_proposal(generator, manifests)
        self.generator = generator

    def adjudicate(self, proposal: ExperimentProposal, state: AdjudicatorView) -> ScopeAssessment:
        valid = (proposal == self.expected and state.claim_id == CLAIM_ID
                 and state.scope.claim_text == TARGET_STATEMENT
                 and state.scope.metric == 'rejection_proportion')
        for cell in proposal.design.cells:
            map_request(cell, generator=self.generator)
        return ScopeAssessment(proposal_id=proposal.proposal_id, adjudicator_id=self.adjudicator_id,
                               status='accepted' if valid else 'rejected', relation='scope_preserving' if valid else 'unresolved',
                               reasons=('Only the attributed finite released-code experimental target is evaluated.',),
                               objective_checks=(('exact_frozen_family_and_target', valid),))


class LabelDegradationEvaluator:
    evaluator_id: str = 'mmdfuse.label-degradation'
    evaluator_version: str = '1'

    def evaluate(self, inputs: ControlComparisonInputs) -> ControlRuleOutcome:
        reference, control = inputs.reference_inputs[0].value, inputs.control_inputs[0].value
        if reference is None or control is None:
            return ControlRuleOutcome(status='not_evaluated', reason_code='missing_measurement')
        passed = control_passes(reference, control, inputs.configuration)
        return ControlRuleOutcome(status='satisfied' if passed else 'failed',
                                  reason_code='frozen_null_band_and_minimum_drop')


class TargetBandVerdict:
    verdict_id: str = 'mmdfuse.T-MF1-engineering-band.v1'
    verdict_version: str = '1'

    def decide(self, measurement: FamilyMeasurement, context: VerdictContext) -> VerdictOutcome:
        if (measurement.registration_digest != context.registration_digest
                or measurement.rule_id != context.decision_rule_id
                or not measurement.coverage_complete or not measurement.controls_satisfied):
            return 'inconclusive'
        return 'holds' if 0.13 <= measurement.value <= 0.23 else 'falsified'
