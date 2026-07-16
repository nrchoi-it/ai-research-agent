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

        interaction = self.client.interactions.create(
            model="gemini-3.5-flash",
            input=f"""{SYSTEM_PROMPT}

User question:
{prompt}
""",
            tools=[
                {
                    "type": "google_search"
                }
            ]
        )

        return {
            "answer": interaction.output_text,
            "interaction": interaction
        }