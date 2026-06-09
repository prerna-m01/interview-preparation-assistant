import re


def extract_score(text):

    match = re.search(
        r"Score:\s*(\d+)/10",
        text,
        re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return 0