"""
BBOX-ADAPTER: Task Prompts and Dataset Loading

Contains the few-shot prompts used for each task (Appendix J) and
dataset loading/splitting code (§F.1, main.py).

Prompts:
- StrategyQA: 2-shot CoT prompt (Appendix J)
- GSM8K: 4-shot prompt from Chain-of-Thought Hub (Appendix J)
- ScienceQA: 1-shot CoT prompt (Appendix J)
- TruthfulQA: 0-shot with system instruction (Appendix J)
- AI feedback selection prompts for each task (Appendix J)
"""

from datasets import load_dataset

# ============================================================
# DATASET LOADING & SPLITTING (§F.1, main.py)
# ============================================================

def load_gsm8k(seed: int = 42):
    """
    Load GSM8K dataset (official train/test splits).
    Train: 7473 samples, Test: 1319 samples.
    Source: Cobbe et al., 2021; paper §F.1; main.py

    Returns:
        (train_dataset, test_dataset)
    """
    train = load_dataset('gsm8k', 'main', split="train").shuffle(seed=seed)
    test = load_dataset('gsm8k', 'main', split="test").shuffle(seed=seed)
    return train, test  # 7473 train / 1319 test


def load_strategyqa(seed: int = 42, train_ratio: float = 0.9):
    """
    Load StrategyQA from wics/strategy-qa (test split only; split into train/eval).
    Train: 2059 samples (~90%), Test: 229 samples (~10%).
    Source: Geva et al., 2021; paper §F.1; main.py; configs/strategyqa.yaml

    Returns:
        (train_dataset, test_dataset)
    """
    dataset = load_dataset('wics/strategy-qa', split="test").shuffle(seed=seed)
    splits = dataset.train_test_split(train_size=train_ratio, shuffle=False)
    return splits['train'], splits['test']  # ~2059 train / ~229 test


def load_truthfulqa(seed: int = 42, train_ratio: float = 0.8777):
    """
    Load TruthfulQA (generation config, validation split).
    Randomly sample 100 questions for test; 717 remaining for training.
    Source: Lin et al., 2022; paper §F.1; main.py; configs/truthfulqa.yaml

    Returns:
        (train_dataset, test_dataset)
    """
    dataset = load_dataset(
        'truthful_qa', 'generation', split="validation"
    ).shuffle(seed=seed)
    splits = dataset.train_test_split(train_size=train_ratio, shuffle=False)
    return splits['train'], splits['test']  # 717 train / 100 test


def load_scienceqa(seed: int = 42, train_size: int = 2000, test_size: int = 500):
    """
    Load ScienceQA (non-image questions only).
    Filter out image questions (x['image'] == None), then select:
    - 2000 training samples from train split
    - 500 test samples from test split
    Source: Lu et al., 2022; paper §F.1; main.py

    Returns:
        (train_dataset, test_dataset)
    """
    train = (
        load_dataset("derek-thomas/ScienceQA", split="train")
        .shuffle(seed=seed)
        .filter(lambda x: x['image'] is None)
        .select(range(train_size))
    )
    test = (
        load_dataset("derek-thomas/ScienceQA", split="test")
        .shuffle(seed=seed)
        .filter(lambda x: x['image'] is None)
        .select(range(test_size))
    )
    return train, test  # 2000 train / 500 test


# ============================================================
# FEW-SHOT PROMPTS (Appendix J)
# ============================================================

STRATEGYQA_PROMPT = """Use the step-by-step method as shown in the examples to answer the question. Break down \
the problem into smaller parts and then provide the final answer (Yes/No) after '####'.

Example 1:
Q: Karachi was a part of Alexander the Great's success?

A: Karachi is a city in modern day Pakistan.
Krokola was an ancient port located in what is now Karachi.
Alexander the Great stationed his fleet in Krokola on his way to Babylon.
Alexander the Great defeated Darius and conquered Babylon before expanding his empire.
#### Yes.

Example 2:
Q: Was P. G. Wodehouse's favorite book The Hunger Games?

A: P. G. Wodehouse died in 1975.
The Hunger Games was published in 2008.
#### No.

Your Question:
Q: <QUESTION>
A:"""
# Source: Appendix J; 2-shot CoT prompt for StrategyQA


GSM8K_PROMPT = """Q: Ivan has a bird feeder in his yard that holds two cups of birdseed. Every week, he has \
to refill the emptied feeder. Each cup of birdseed can feed fourteen birds, but Ivan is \
constantly chasing away a hungry squirrel that steals half a cup of birdseed from the \
feeder every week. How many birds does Ivan's bird feeder feed weekly?
A: Let's think step by step.
The squirrel steals 1/2 cup of birdseed every week, so the birds eat 2 - 1/2 = 1 1/2 cups of birdseed.
Each cup feeds 14 birds, so Ivan's bird feeder feeds 14 * 1 1/2 = 21 birds weekly.
#### The answer is 21

Q: Samuel took 30 minutes to finish his homework while Sarah took 1.3 hours to finish it. \
How many minutes faster did Samuel finish his homework than Sarah?
A: Let's think step by step.
Since there are 60 minutes in 1 hour, then 1.3 hours is equal to 1.3 x 60 = 78 minutes.
Thus, Samuel is 78 - 30 = 48 minutes faster than Sarah.
#### The answer is 48

Q: Julia bought 3 packs of red balls, 10 packs of yellow balls, and 8 packs of green balls. \
There were 19 balls in each package. How many balls did Julie buy in all?
A: Let's think step by step.
The total number of packages is 3 + 10 + 8 = 21.
Julia bought 21 × 19 = 399 balls.
#### The answer is 399

Q: Lexi wants to run a total of three and one-fourth miles. One lap on a particular outdoor track \
measures a quarter of a mile around. How many complete laps must she run?
A: Let's think step by step.
There are 3/ 1/4 = 12 one-fourth miles in 3 miles.
So, Lexi will have to run 12 (from 3 miles) + 1 (from 1/4 mile) = 13 complete laps.
#### The answer is 13

Q: <QUESTION>
A: Let's think step by step."""
# Source: Appendix J; 4-shot prompt from Chain-of-Thought Hub
# https://github.com/FranxYao/chain-of-thought-hub/blob/main/gsm8k/lib_prompt/prompt_simple_4_cases.txt


SCIENCEQA_PROMPT = """Use the step-by-step method as shown in the example to answer the question. Respond \
to the question by adhering to the given format: provide step-by-step reasoning (one sentence per line), \
then give the final answer after '####'.

Example:
Question: Which figure of speech is used in this text?
Dr. Shelton is unhappy with her new assistant because simple tasks, like fetching coffee, take him years to finish.
Choices:
0: anaphora
1: hyperbole

Answer: The text uses hyperbole, an obvious exaggeration that is not meant to be taken literally.
Take him years to finish is an exaggeration, since it probably does not take him entire years to fetch coffee.
#### 1

Your Question:
<QUESTION>"""
# Source: Appendix J; 1-shot CoT prompt for ScienceQA


TRUTHFULQA_PROMPT = """You are a helpful, respectful and honest assistant. Always answer as helpfully as \
possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, \
dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something \
not correct. If you don't know the answer to a question, please don't share false information.

Q: <QUESTION>
A:"""
# Source: Appendix J; 0-shot system instruction for TruthfulQA (same as Liu et al., 2024)


# ============================================================
# AI FEEDBACK SELECTION PROMPTS (Appendix J)
# ============================================================

STRATEGYQA_AI_FEEDBACK_PROMPT = """**Task** As an expert rater, evaluate and select the best answer for the \
question based on chain-of-thought reasoning. Use the criteria of coherency, reasonability, correctness, \
and format to guide your selection.

**Question** <QUESTION>

<CANDIDATE_ANSWERS>

**Example of a Good Answer**
Q: Karachi was a part of Alexander the Great's success?
A: Karachi is a city in modern day Pakistan.
Krokola was an ancient port located in what is now Karachi.
Alexander the Great stationed his fleet in Krokola on his way to Babylon.
Alexander the Great defeated Darius and conquered Babylon before expanding his empire.
#### Yes.

**Criteria for a Good Answer**
- Coherency: The answer should present logical step-by-step reasoning that is coherent and directly related to the question.
- Reasonability: The answer should provide logical and factual reasoning steps leading to the final conclusion.
- Correctness: The final answer should be correct.
- Format: Each reasoning step should be in a separate sentence, ending with a definitive answer (must be either '#### Yes.' or '#### No.').

**Your Task**
Select the best answer based on the provided criteria, with a one-sentence explanation.
Use this format:
Best Answer and Explanation: [Candidate Answer _]: [Explanation]

**Your Answer**
Best Answer and Explanation: ["""
# Source: Appendix J


GSM8K_AI_FEEDBACK_PROMPT = """**Task** As an expert rater, evaluate and select the best answer for the \
question based on chain-of-thought reasoning. Use the criteria of coherency, reasonability, correctness, \
and format to guide your selection.

**Question** <QUESTION>

<CANDIDATE_ANSWERS>

**Criteria for a Good Answer**
- Coherency: The answer should present logical step-by-step reasoning coherent and directly related to the question.
- Reasonability: The answer should provide logical and factual reasoning steps leading to the final conclusion.
- Correctness: The final answer should be correct.
- Format: Each reasoning step should be in a separate sentence, ending with a numerical answer after '####'.

**Your Task**
Select the best answer based on the provided criteria, with a one-sentence explanation.
Use this format:
Best Answer and Explanation: [Candidate Answer _]: [Explanation]

**Your Answer**
Best Answer and Explanation: ["""
# Source: Appendix J


TRUTHFULQA_AI_FEEDBACK_PROMPT = """**Task** As an expert rater, evaluate and select the top 5 truthful and \
informative answers for the question. Use the criteria illustrated below to guide your selection.

**Question** <QUESTION>

<CANDIDATE_ANSWERS>

**Criteria for a Good Answer**
- The selected answers should be as helpful as possible, while being safe.
- The selected answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.
- If a question does not make any sense, or is not factually coherent, the selected answer should explain why.

**Your Task**
Select top 5 answers based on the provided criteria, with a one-sentence explanation.
Use this format:
The Best Answer and Explanation: [Candidate Answer _]: [Explanation]
The 2nd Best Answer and Explanation: [Candidate Answer _]: [Explanation]
...

**Your Answer**
The Best Answer and Explanation: ["""
# Source: Appendix J


SCIENCEQA_AI_FEEDBACK_PROMPT = """**Task** As an expert rater, evaluate and select the best answer for the \
question based on chain-of-thought reasoning. Use the criteria of coherency, reasonability, correctness, \
and format to guide your selection.

**Question** <QUESTION>

<CANDIDATE_ANSWERS>

**Criteria for a Good Answer**
- Coherency: The answer should present logical step-by-step reasoning coherent and directly related to the question.
- Reasonability: The answer should provide logical and factual reasoning steps leading to the final conclusion.
- Correctness: The final answer should be correct.
- Format: Each reasoning step should be in a separate sentence, ending with a numerical answer after '####'.

**Your Task**
Select the best answer based on the provided criteria, with a one-sentence explanation.
Use this format:
Best Answer and Explanation: [Candidate Answer _]: [Explanation]

**Your Answer**
Best Answer and Explanation: ["""
# Source: Appendix J


# ============================================================
# COST TRACKING (§4.4, Table 4)
# ============================================================

def compute_inference_cost_per_1k(
    total_input_tokens: int,
    total_output_tokens: int,
    num_questions: int,
    input_cost_per_1k_tokens: float = 0.001,   # gpt-3.5-turbo-1106 rate
    output_cost_per_1k_tokens: float = 0.002,  # gpt-3.5-turbo-1106 rate
) -> float:
    """
    Compute inference cost per 1000 questions from token usage statistics.
    As described in Table 4 footnote (§4.4):
    "inference cost was calculated by aggregating the total token consumption
    statistics provided by Azure API and subsequently applying the cost per
    token (gpt-3.5-turbo-1106) as specified in the OpenAI official documentation."

    Args:
        total_input_tokens: Total prompt tokens consumed across all questions
        total_output_tokens: Total completion tokens consumed across all questions
        num_questions: Number of questions evaluated
        input_cost_per_1k_tokens: OpenAI rate for prompt tokens
        output_cost_per_1k_tokens: OpenAI rate for completion tokens

    Returns:
        cost_per_1k_questions: USD cost per 1000 questions
    """
    total_cost = (
        (total_input_tokens / 1000) * input_cost_per_1k_tokens
        + (total_output_tokens / 1000) * output_cost_per_1k_tokens
    )
    cost_per_question = total_cost / num_questions
    cost_per_1k_questions = cost_per_question * 1000
    return cost_per_1k_questions


class APICostTracker:
    """
    Tracks and logs API costs during inference and evaluation.
    Mirrors token_usage tracking in llms/api.py (LLM_API class).
    """

    def __init__(self):
        self.input_tokens = 0
        self.output_tokens = 0
        self.num_queries = 0

    def log_usage(self, prompt_tokens: int, completion_tokens: int) -> None:
        """Log token usage for a single API call."""
        self.input_tokens += prompt_tokens
        self.output_tokens += completion_tokens
        self.num_queries += 1

    def get_cost_per_1k(
        self,
        num_questions: int,
        input_rate: float = 0.001,
        output_rate: float = 0.002,
    ) -> float:
        """
        Compute cost per 1000 questions from logged usage.
        Source: §4.4, Table 4 footnote.
        """
        return compute_inference_cost_per_1k(
            self.input_tokens, self.output_tokens,
            num_questions, input_rate, output_rate,
        )

    def reset(self) -> None:
        self.input_tokens = 0
        self.output_tokens = 0
        self.num_queries = 0
