from collections import Counter

from sqlalchemy import func

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

    def get_total_interviews(self, db):

        return db.query(
            InterviewRecord
        ).count()

    def get_average_score(self, db):

        return db.query(
            func.avg(InterviewRecord.score)
        ).scalar()

    def get_highest_score(self, db):

        return db.query(
            func.max(InterviewRecord.score)
        ).scalar()

    def get_lowest_score(self, db):

        return db.query(
            func.min(InterviewRecord.score)
        ).scalar()

    def get_common_weak_topics(self, db):

        records = db.query(
            InterviewRecord
        ).all()

        topics = []

        for record in records:

            if not record.weak_topics:
                continue

            topic_list = record.weak_topics.split(",")

            for topic in topic_list:

                topic = topic.strip()

                if topic:
                    topics.append(topic)

        counter = Counter(topics)

        return [
            {
                "topic": topic,
                "count": count
            }
            for topic, count in counter.most_common()
        ]