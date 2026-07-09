# Algorithm

## Mathematical Formulation

### Task Definition
A task $\mathcal{T}_i = (Q_i, M_i, R_i^{\text{masked}}, G_i)$ where:
- $Q_i$: research question (natural language)
- $M_i$: high-level method description (natural language)  
- $R_i^{\text{masked}} = R_i \setminus F_i^{\text{mask}}$: masked repository
- $G_i = (D_i^{gt}, \Delta_i^{gt}, C_i^{gt})$: ground truth (design, diff, conclusion)

### Scoring
Agent output: $\hat{G}_i = (\hat{D}_i, \hat{\Delta}_i, \hat{C}_i)$

Individual metrics:
$$D_i = \frac{|\{v \in D_i^{gt} : \text{LLM-judge matches } v \text{ in } \hat{D}_i\}|}{|D_i^{gt}|} \times 100$$

$$I_i = \frac{|\{r \in \Delta_i^{gt} : \text{LLM-judge satisfies } r \text{ in } \hat{\Delta}_i\}|}{|\Delta_i^{gt}|} \times 100$$

$$C_i = \mathbb{1}[\text{LLM-judge}(\hat{C}_i, C_i^{gt}) = \text{correct}]$$

$$E_i = \mathbb{1}[\text{CodeExecutor}(R_i, \hat{\Delta}_i) = \text{success}]$$

Conjunctive metrics:
$$\text{All}^\checkmark_i = \mathbb{1}[D_i > 0 \wedge I_i > 0 \wedge C_i = 1]$$
$$\text{All·E}^\checkmark_i = \mathbb{1}[D_i > 0 \wedge I_i > 0 \wedge C_i = 1 \wedge E_i = 1]$$
$$(I \cdot E)_i = \mathbb{1}[I_i > 0 \wedge E_i = 1]$$

Aggregated over $N$ tasks:
$$\bar{D} = \frac{1}{N}\sum_{i=1}^N D_i, \quad \bar{I} = \frac{1}{N}\sum_{i=1}^N I_i, \text{ etc.}$$

### Multi-Pass Extraction Algorithm

```
Algorithm: SemiAutomatedTaskCuration(paper_pdf, repo)

Input: paper_pdf (PDF document), repo (GitHub repository URL)

Stage 1: Source Filtering
  if citation_count(paper) < threshold OR stars(repo) < threshold:
    return None  # Filtered out

Stage 2.1: Multi-Modal Research Task Extraction
  # Index PDF
  indexed_pdf ← OCR(paper_pdf) + multimodal_extract(tables, figures, headers)
  
  # Pass 1: High-level takeaways via RAG
  takeaways ← RAG_query(indexed_pdf, query="main research questions and contributions")
  
  # Pass 2: Subsection-level semantic extraction
  context ← {}
  tasks_raw ← []
  for section in evaluation_sections(indexed_pdf):
    label ← classify(section, classes=["implementation_context", "research_question"])
    if label == "implementation_context":
      context.add(section)
    else:
      task_raw ← extract_task(section, context=context, tables=indexed_pdf.tables)
      tasks_raw.append(task_raw)
  
  # Pass 3: Full-paper re-querying for missed details
  for task in tasks_raw:
    task ← refine(task, full_paper=indexed_pdf, appendix=indexed_pdf.appendix)
  
  Output: [(Q, M, D_gt, C_gt)] per task

Stage 2.2: Implementation Extraction
  agent ← ToolAugmentedAgent(tools=[PDF_reader, terminal, web_browser])
  
  for task (Q, M, D_gt, C_gt) in tasks_raw:
    candidate ← None
    while candidate is None or not executable:
      candidate ← agent.search(repo, goal=(Q, M, C_gt))
      # candidate = (script_list, usage_instructions)
      executable ← execute_in_container(candidate)
      if not executable:
        agent.refine(candidate)  # iterative refinement
    
    # AST tracing to extract step-by-step requirements
    Δ_gt ← AST_trace(candidate.scripts) → natural_language_steps
    additional_context ← extract_hyperparams(repo.configs, repo.README)
    task.update(Δ_gt, additional_context)

Stage 3: Verification
  for task in tasks:
    result ← execute_in_container(task.Δ_gt)
    if result != expected_output:
      task ← Stage_2(task)  # loop back
    else:
      apply_masking(task, F_mask)  # scripted git operations
      human_review(task)  # lightweight consistency check
      dataset.add(task)

Output: EXP-Bench dataset of verified tasks
```

### Conjunctive Evaluation Algorithm

```
Algorithm: EvaluateAgent(agent, task_set)

Input: agent (LLM-based agent), task_set (EXP-Bench tasks)

for task T_i in task_set:
  # Setup
  container ← fresh_docker_container(ubuntu_24_04, 4xA40)
  R_masked ← apply_masking(clone(task.repo), task.F_mask)
  
  # Agent execution
  agent_output ← agent.run(Q=task.Q, M=task.M, R=R_masked, 
                            timeout=40_minutes)
  logs ← collect_logs(agent_output)
  
  # Monitor check
  M_i ← monitor_check(logs)  # o3-mini
  if M_i == 0:
    discard(task_i); continue
  
  # LLM Judge evaluation (chunked for long inputs)
  chunks ← chunk(agent_output + logs, max_context_len)
  D_i, C_i, I_i ← 0, 0, 0
  for chunk in chunks:
    D_i, C_i ← judge.evaluate_design_conclusion(chunk, G_i.D_gt, G_i.C_gt)
    I_i ← judge.evaluate_implementation(chunk, G_i.Δ_gt)
  
  # Code execution
  E_i ← executor.run(R_i, agent_output.Δ_agent)
  
  # Conjunctive metrics
  scores[i] ← {D: D_i, I: I_i, C: C_i, E: E_i,
                IE: I_i∧E_i, All: D_i∧I_i∧C_i, AllE: D_i∧I_i∧C_i∧E_i}

return aggregate(scores)
```

## Complexity Analysis

- **Dataset Curation**: $O(P \cdot (T_{\text{OCR}} + T_{\text{LLM}} \cdot S + T_{\text{exec}}))$ where $P$ = number of papers, $S$ = number of subsections per paper, $T_{\text{exec}}$ = container execution time. Practical cost: ~$60 USD/paper + ~20 min human time.
- **Agent Evaluation**: $O(N \cdot T_{\text{agent}})$ where $N$ = 461 tasks, $T_{\text{agent}}$ ≤ 40 minutes. LLM judge adds $O(N \cdot L / C)$ where $L$ = log/diff length, $C$ = chunk size.
