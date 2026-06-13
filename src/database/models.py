from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class InterviewRecord(Base):
    __tablename__ = "interview_records"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question = Column(
        Text,
        nullable=False
    )

    candidate_answer = Column(
        Text,
        nullable=False
    )

    evaluation = Column(
        Text,
        nullable=False
    )

    score = Column(
        Integer,
        nullable=False
    )

    weak_topics = Column(
        Text,
        nullable=True
    )