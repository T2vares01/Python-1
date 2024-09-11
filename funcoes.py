from crewai import Agent, Task, Crew
from crewai_tools import tool,BaseTool

@tool
def web():
    pass

hand = Agent(
    role = "",
    goal = "",
    backstory = "",
    tools = [web]
)

web = Task(
    description = '',
    expected_output = '',
    agent = Agent
)

crew = Crew(
    agents=[hand],
    tasks=[web],
    verbose=True
)

# Execute tasks
crew.kickoff()

