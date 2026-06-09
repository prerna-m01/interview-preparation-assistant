from src.components.evaluator import Evaluator

evaluator = Evaluator()

result = evaluator.evaluate_answer(
    question="What is Overfitting?",
    candidate_answer="Overfitting occurs when a model memorizes training data."
)

print(result)