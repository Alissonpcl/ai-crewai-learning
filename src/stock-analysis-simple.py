import os

from crewai import Agent, Task, Crew
from dotenv import load_dotenv
# Usando o ChatLiteLLM em vez de LiteLLM
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

# Definindo os agentes
analista_financeiro = Agent(
    role="Analista Financeiro",
    goal="Analisar dados financeiros e fundamentalistas de empresas",
    backstory="Você é um analista financeiro experiente com foco em análise fundamentalista e balanços",
    verbose=True,
    llm=llm
)

analista_tecnico = Agent(
    role="Analista Técnico",
    goal="Analisar padrões de preços e volumes para identificar tendências",
    backstory="Você é especializado em encontrar padrões em gráficos e indicadores técnicos",
    verbose=True,
    llm=llm
)

redator_financeiro = Agent(
    role="Redator Financeiro",
    goal="Transformar análises técnicas em relatórios claros e concisos",
    backstory="Você transforma dados complexos em narrativas compreensíveis",
    verbose=True,
    llm=llm
)

# Definindo as tarefas
tarefa_analise_fundamental = Task(
    description="Analisar os fundamentais da empresa {empresa}, incluindo P/L, ROE, margem líquida e crescimento de receita",
    expected_output="Um relatório detalhado sobre a saúde financeira da empresa",
    agent=analista_financeiro
)

tarefa_analise_tecnica = Task(
    description="Analisar os gráficos de preço e volume da {empresa} nos últimos 6 meses, identificando suportes, resistências e tendências",
    expected_output="Um relatório técnico com pontos de entrada e saída potenciais",
    agent=analista_tecnico
)

tarefa_relatorio_final = Task(
    description="Criar um relatório final combinando a análise fundamental e técnica para a empresa {empresa}",
    expected_output="Um relatório completo de investimento com recomendações claras",
    agent=redator_financeiro
)

# Configurando a equipe (crew)
equipe_analise = Crew(
    agents=[analista_financeiro, analista_tecnico, redator_financeiro],
    tasks=[tarefa_analise_fundamental, tarefa_analise_tecnica, tarefa_relatorio_final],
    verbose=True
)

# Executando a análise
if __name__ == "__main__":
    empresa = "AAPL"  # Pode ser substituída por qualquer ticker

    # Substituindo o placeholder nas descrições das tarefas
    tarefa_analise_fundamental.description = tarefa_analise_fundamental.description.format(empresa=empresa)
    tarefa_analise_tecnica.description = tarefa_analise_tecnica.description.format(empresa=empresa)
    tarefa_relatorio_final.description = tarefa_relatorio_final.description.format(empresa=empresa)

    # Executando a equipe
    resultado = equipe_analise.kickoff()
    print("Relatório final:")
    print(resultado)