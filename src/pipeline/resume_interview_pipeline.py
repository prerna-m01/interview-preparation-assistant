from src.components.resume_parser import ResumeParser
from src.components.question_generator import QuestionGenerator


class ResumeInterviewPipeline:

    def __init__(self):

        self.parser = ResumeParser()

        self.question_generator = QuestionGenerator()

    def generate_resume_questions(
        self,
        resume_path
    ):

        text = self.parser.extract_text(
            resume_path
        )

        skills = self.parser.extract_skills(
            text
        )

        print("\nDetected Skills:")
        print(skills)

        for skill in skills:

            print(f"\nQuestions for {skill}:")

            questions = self.question_generator.generate_questions(
                skill,
                3
            )

            print(questions)