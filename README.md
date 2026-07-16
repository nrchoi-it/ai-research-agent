# AI Research Agent

A Python-based AI research assistant powered by Google Gemini.

This project researches user questions, generates AI-powered responses, and automatically saves the results as Markdown reports. It is designed as the foundation for a more advanced research agent supporting document analysis, RAG, and multi-source reasoning.

## Features

- Google Gemini API
- Gemini Interactions API
- Google Search Tool
- Markdown report generation
- Interactive command-line interface

## Project Structure

```
AI-Research-Agent/
├── agents/
├── data/
├── docs/
├── reports/
├── tools/
├── app.py
├── requirements.txt
└── README.md
```

## Getting Started

```bash
pip install -r requirements.txt
python app.py
```

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

## Example

```
Question > Explain the Korean AI Framework Act.

...

Report saved:
reports/2026-07-17_00-15-30.md
```

## Roadmap

**v1**
- Google Gemini Integration
- Google Search Tool
- Markdown Report Generation

**v2**
- PDF Analysis
- Retrieval-Augmented Generation (RAG)
- Multi-document Research

**v3**
- Web Interface
- Deployment