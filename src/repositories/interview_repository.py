from src.database.models import InterviewRecord


class InterviewRepository:

    def save(
        self,
        db,
        question,
        candidate_answer,
        evaluation,
        score
    ):

        record = InterviewRecord(
            question=question,
            candidate_answer=candidate_answer,
            evaluation=evaluation,
            score=score
        )

        db.add(record)
        db.commit()

    def get_all(self, db):

        return db.query(
            InterviewRecord
        ).all()