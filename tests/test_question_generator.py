from src.components.question_generator import QuestionGenerator

generator = QuestionGenerator()

questions = generator.generate_questions(
    topic="Machine Learning",
    num_questions=3
)

print("Generated Questions:\n")

for i, question in enumerate(questions, start=1):
    print(f"{i}. {question}")