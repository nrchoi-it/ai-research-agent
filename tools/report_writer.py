from pathlib import Path
from datetime import datetime


class ReportWriter:

    def __init__(self):
        self.report_dir = Path("reports")
        self.report_dir.mkdir(exist_ok=True)

    def save(self, question: str, answer: str) -> str:

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = self.report_dir / f"{timestamp}.md"

        content = f"""# AI Research Report

## Question

{question}

---

## Answer

{answer}
"""

        filename.write_text(content, encoding="utf-8")

        return str(filename)