import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("openai_api_key")
if not api_key:
    raise RuntimeError("A variável openai_api_key não foi encontrada ou está vazia no arquivo .env.")

client = OpenAI(api_key=api_key, base_url="https://api.mistral.ai/v1")

def perguntar_ai(mensagem):
    resposta = client.chat.completions.create(
        model="mistral-small-latest",
        messages=[
            {"role": "system", "content": "Chatbot de Terminal"},
            {"role": "user", "content": mensagem}
        ]
    )
    return resposta.choices[0].message.content

def main():

    print("Bem-vindo criador! Como posso ajudar?")

    while True:
        msg = input("Você: ")
        
        if msg.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chatbot. Até logo!")
            break

        resposta = perguntar_ai(msg)
        print("Chatbot:", resposta)


if __name__ == "__main__":
    main()