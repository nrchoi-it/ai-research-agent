from agents.research_agent import ResearchAgent


def main():

    agent = ResearchAgent()

    print("=" * 50)
    print("AI Research Agent")
    print("To exit, enter 'exit'.")
    print("=" * 50)

    while True:

        question = input("\nQuestion > ")

        if question.lower() == "exit":
            print("Exiting the program..")
            break

        answer, report_path = agent.research(question)

        print("\n" + "=" * 50)
        print(answer)
        print("=" * 50)
        print(f"Report saved: {report_path}")


if __name__ == "__main__":
    main()