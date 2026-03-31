from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

agno_assist = Agent(
    name="H.I.V.E.",
    model=Groq(id="llama-3.3-70b-versatile"),
    db=SqliteDb(db_file="agno.db"),
    tools=[MCPTools(url="https://docs.agno.com/mcp")],
    instructions="""
    Você é uma astróloga, especializada em horóscopo e signos.
    O usuário informará a data de nascimento.
    Responda com:
    - seu signo
    - horóscopo do dia
    - curiosidade curta
    """,
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True,
)

print("Digite 'sair' para encerrar\n")

while True:
    pergunta = input("Qual sua data de nascimento ? ")

    if pergunta.lower() == "sair":
        break

    resposta = agno_assist.run(pergunta)

    print(f"\nAgente:\n{resposta.content}\n")

agent_os = AgentOS(agents=[agno_assist])
app = agent_os.get_app()