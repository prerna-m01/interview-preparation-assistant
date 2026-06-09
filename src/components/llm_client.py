import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


class LLMClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(self, prompt):

        for attempt in range(3):

            try:

                response = self.model.generate_content(
                    prompt
                )

                return response.text

            except Exception as e:

                if "503" in str(e):

                    time.sleep(5)

                    continue

                return f"LLM Error: {str(e)}"

        return "LLM Error: Model unavailable after retries."