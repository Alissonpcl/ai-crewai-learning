import os

from ollama import ChatResponse
from ollama import Client

os.environ['OLLAMA_HOST'] = 'http://192.168.1.24:11434'

client = Client(
    host='http://192.168.1.24:11434',
    headers={'x-some-header': 'some-value'}
)

response: ChatResponse = client.chat(model='llama3.1:latest', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)