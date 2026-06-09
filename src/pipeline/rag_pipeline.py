from src.components.retriever import Retriever
from src.components.llm_client import LLMClient

class RAGPipeline:

    def __init__(self, retriever):

        self.retriever = retriever
        self.llm = LLMClient()

    def answer_question(self, question):

        chunks = self.retriever.retrieve(
            question,
            top_k=3
        )

        context = "\n\n".join(chunks)

        prompt = f"""
        You are an ML Interview Assistant.

        Use the provided context to answer the question.

        If the context does not contain enough information,
        use your general machine learning knowledge.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        return self.llm.generate(prompt)