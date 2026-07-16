import os

from dotenv import load_dotenv
from google import genai
from tools.prompts import SYSTEM_PROMPT

load_dotenv()


class LLM:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def ask(self, prompt: str):

        response = self.client.models.generate_content(
            model="gemini-flash-latest",
            contents=f"""{SYSTEM_PROMPT}

        사용자 질문:
        {prompt}
        """
        )

        return response.text