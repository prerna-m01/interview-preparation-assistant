from src.components.interview_history import InterviewHistory

history = InterviewHistory()

results = [
    {
        "question": "What is Machine Learning?",
        "candidate_answer": "ML is a subset of AI",
        "score": 8
    }
]

path = history.save_interview(
    results
)

print("Saved:", path)