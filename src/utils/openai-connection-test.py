"""
Simple Python code to validate connection and credentials with LLM API
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Set up your API key
# Replace with your actual API key or set it as an environment variable
API_KEY = os.environ.get('LITELLM_KEY')
BASE_URL = os.environ.get('LITELLM_API_BASE')

# print(API_KEY, BASE_URL)
# exit(0)

# Inicializar o cliente OpenAI
# Substitua com sua chave de API ou configure como uma variável de ambiente
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def get_openai_response(prompt, model="gpt-3.5-turbo"):
    """
    Envia um prompt para a API OpenAI e obtém uma resposta.

    Args:
        prompt (str): O prompt a ser enviado para a API
        model (str): O modelo a ser usado para a requisição

    Returns:
        str: A resposta de texto da API
    """
    try:
        # Criar uma requisição de chat completion
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )

        # Extrair o texto da resposta
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

def main():
    # Exemplo de prompt
    user_prompt = "Explique computação quântica em termos simples."

    print("Enviando prompt para a API OpenAI:", user_prompt)
    print("\nObtendo resposta...\n")

    # Obter e imprimir a resposta
    response = get_openai_response(user_prompt)
    print("Resposta da OpenAI:")
    print("-" * 50)
    print(response)
    print("-" * 50)

if __name__ == "__main__":
    main()