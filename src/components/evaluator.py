from src.components.llm_client import LLMClient


class Evaluator:

    def __init__(self):

        self.llm = LLMClient()

    def evaluate_answer(
        self,
        question,
        candidate_answer
    ):
    
        prompt = f"""
        You are an experienced technical interviewer.

        Evaluate the candidate's answer.

        Question:
        {question}

        Candidate Answer:
        {candidate_answer}

        Return the response EXACTLY in this format:

        Correctness: <Correct / Partially Correct / Incorrect>

        Score: <number>/10

        Strengths:
        - point 1
        - point 2

        Weaknesses:
        - point 1
        - point 2

        Ideal Answer:
        <ideal answer>
        """

        return self.llm.generate(prompt)