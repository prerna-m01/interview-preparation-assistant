import json
import os
from datetime import datetime


class InterviewHistory:

    def save_interview(self, results):

        os.makedirs(
            "data/interviews",
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        filepath = (
            f"data/interviews/interview_{timestamp}.json"
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                results,
                file,
                indent=4
            )

        return filepath