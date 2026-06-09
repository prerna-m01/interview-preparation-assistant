from src.components.question_generator import QuestionGenerator
from src.components.evaluator import Evaluator
from src.components.report_generator import ReportGenerator
from src.utils import extract_score


class InterviewPipeline:

    def __init__(self):

        self.question_generator = QuestionGenerator()
        self.evaluator = Evaluator()
        self.report_generator = ReportGenerator()

    def start_interview(
        self,
        topic,
        num_questions=1
    ):

        questions = self.question_generator.generate_questions(
            topic,
            num_questions
        )

        question_list = questions

        results = []

        for question in question_list:

            if not question.strip():
                continue

            print("\n" + "=" * 50)
            print(question)

            candidate_answer = input(
                "\nYour Answer: "
            )

            result = self.evaluator.evaluate_answer(
            question,
            candidate_answer
            )

            score = extract_score(
                result
            )

            results.append(
                {
                    "question": question,
                    "score": score
                }
            )

        report = self.report_generator.generate_report(
            results
        )

        print("\n")
        print(report)