class ReportGenerator:

    def generate_report(self, results):

        if not results:
            return "No interview results available."

        total_score = 0

        for result in results:
            total_score += result["score"]

        average_score = total_score / len(results)

        report = f"""
Interview Summary
=================

Questions Attempted: {len(results)}

Average Score: {average_score:.2f}/10
"""

        return report