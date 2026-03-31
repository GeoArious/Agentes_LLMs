from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

agno_assist = Agent(
    name="The_Clima",
    model=Groq(id="llama-3.3-70b-versatile"),
    db=SqliteDb(db_file="agno.db"),
    tools=[MCPTools(url="https://docs.agno.com/mcp")],
    instructions="""
    Você é um climatólogo, especializado no clima e tempo da cidade de teresina, no estado do Piauí, Brasil.
    Informe o clima da cidade no dia de hoje.
    """,
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True,
)


clima = agno_assist.run("Resposta curta")

print(f"\nAgente:\n{clima.content}\n")

agent_os = AgentOS(agents=[agno_assist])
app = agent_os.get_app()