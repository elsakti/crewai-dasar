import os
from crewai import Agent, Task, Crew;

os.environ["OPENAI_API_KEY"] = "HEHE HEHA"
os.environ["OPENAI_MODEL_NAME"] = "gpt-4"

info_agent = Agent (
    role="Historian Agent",
    goal="Give me the World History information I need to complete the task",
    backstory=
    """

    You are a helpful assistant that provides information to complete a task

    """
)

task1 = Task(
    description="Tell me about the history of Borobudur.",
    expected_output=
    """
    
    The history of Borobudur is a
    long and complex one, with influences from many
    different cultures and civilizations. The earliest 
    known inhabitants of the Borobudur archipelago were 
    the Austronesian peoples, who arrived around 5,000 years
    ago. The first major civilization in the region was the
    Majapahit Empire, which flourished from the 13th to the 
    16th centuries. The empire was a major center of trade and
    culture, and its influence can still be seen in the architecture
    , art, and music of the region today.
    
    """,
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose=True
)

result = crew.kickoff()

