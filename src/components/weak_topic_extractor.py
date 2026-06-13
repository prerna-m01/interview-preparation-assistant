import re

class WeakTopicExtractor:

    def extract(self, evaluation):

        pattern = r"Weaknesses:(.*?)(Ideal Answer:|$)"

        match = re.search(
            pattern,
            evaluation,
            re.DOTALL
        )

        if not match:
            return []

        weaknesses = match.group(1)

        topics = []

        for line in weaknesses.split("\n"):

            line = line.strip()

            if line.startswith("-"):
                topics.append(
                    line.replace("-", "").strip()
                )

        return topics