from src.components.resume_parser import ResumeParser

parser = ResumeParser()

text = parser.extract_text(
    "data/raw/resume.pdf"
)

print(text[:2000])