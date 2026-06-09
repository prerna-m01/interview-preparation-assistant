from src.components.llm_client import LLMClient

llm = LLMClient()

response = llm.generate(
    "What is Machine Learning?"
)

print(response)