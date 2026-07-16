from tools.llm import LLM


class ResearchAgent:

    def __init__(self):
        self.llm = LLM()

    def research(self, question):

        answer = self.llm.ask(question)

        return answer