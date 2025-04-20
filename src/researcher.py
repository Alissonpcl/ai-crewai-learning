import os

from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from langchain_community.chat_models import ChatLiteLLM

load_dotenv()

# URL personalizada para sua instância do LiteLLM
LITELLM_API_BASE = os.environ.get("LITELLM_API_BASE")
LITELLM_KEY = os.environ.get("LITELLM_KEY")

# Configuração do LLM usando ChatLiteLLM via LangChain com URL customizada
llm = ChatLiteLLM(
    model_name="gpt-4",  # ou outro modelo compatível
    temperature=0.7,
    api_key=LITELLM_KEY,  # Substitua pela sua chave API
    api_base=LITELLM_API_BASE  # URL customizada para sua instância LiteLLM
)

researcher = Agent(
    role="Pesquisador",
    goal="Coletar informações sobre tendências de IA",
    backstory="Especialista em tecnologia e inovação",
    llm=llm
)

writer = Agent(
    role="Redator",
    goal="Escrever um artigo claro e envolvente",
    backstory="Experiente redator de tecnologia",
    llm=llm
)

task1 = Task(
    agent=researcher,
    description="Pesquisar 5 tendências emergentes em IA em 2025.",
    expected_output="Uma lista com pelo menos 5 tendências de IA, cada uma com uma breve explicação."
)

task2 = Task(
    agent=writer,
    description="Escrever um artigo com base nas tendências encontradas.",
    expected_output="Um artigo bem estruturado com introdução, tópicos explicativos sobre as tendências e conclusão."
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True
)

resultado = crew.kickoff()
print("Relatório final:")
print(resultado)
