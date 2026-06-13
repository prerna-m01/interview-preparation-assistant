from src.database.models import InterviewRecord


class InterviewRepository:

    def save(
        self,
        db,
        question,
        candidate_answer,
        evaluation,
        score,
        weak_topics
    ):

        record = InterviewRecord(
            question=question,
            candidate_answer=candidate_answer,
            evaluation=evaluation,
            score=score,
            weak_topics=weak_topics
        )

        db.add(record)
        db.commit()

    def get_all(self, db):

        return db.query(
            InterviewRecord
        ).all()