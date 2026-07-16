from tools.llm import LLM
from tools.report_writer import ReportWriter


class ResearchAgent:

    def __init__(self):
        self.llm = LLM()
        self.report_writer = ReportWriter()

    def research(self, question):

        result = self.llm.ask(question)

        report_path = self.report_writer.save(
            question=question,
            answer=result["answer"]
        )

        return result["answer"], report_path