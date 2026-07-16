from agents.research_agent import ResearchAgent

agent = ResearchAgent()

answer = agent.research(
    "AI 기본법을 간단히 설명해줘."
)

print(answer)