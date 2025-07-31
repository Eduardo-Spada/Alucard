import requests
import base64
import os
import sys

def get_image_description(image_path):
    # Pegando o token da variável de ambiente
    hf_token = os.getenv("HF_TOKEN")

    # Verifica se o token existe
    if not hf_token:
        return "Erro: o token HF_TOKEN não está definido. Defina com os.environ ou no ambiente do sistema."

    # Endpoint da API
    url = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"

    # Headers da requisição
    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }

    # Lê e codifica a imagem
    try:
        with open(image_path, "rb") as image_file:
            img_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        return f"Erro: imagem não encontrada em '{image_path}'"
    except Exception as e:
        return f"Erro ao ler a imagem: {str(e)}"

    # Prepara o payload
    payload = {
        "inputs": {
            "image": img_base64
        }
    }

    # Faz a requisição
    try:
        response = requests.post(url, headers=headers, json=payload)
    except requests.exceptions.RequestException as e:
        return f"Erro na conexão com a API: {str(e)}"

    # Analisa a resposta
    if response.status_code == 200:
        try:
            result = response.json()
            print("DEBUG:", result)
            return result[0]["generated_text"]
        except (KeyError, IndexError):
            return "Erro: resposta inesperada da API."
    elif response.status_code == 401:
        return "Erro 401: Token inválido ou expirado."
    elif response.status_code == 403:
        return "Erro 403: Acesso negado. Verifique permissões do token."
    elif response.status_code == 404:
        return "Erro 404: Modelo não encontrado ou caminho errado."
    else:
        return f"Erro {response.status_code}: {response.text}"


# Exemplo de uso:
if __name__ == "__main__":
    image_path = "exemplo.jpg"  # Altere aqui pro nome da imagem que você quer testar
    descricao = get_image_description(image_path)
    print("Descrição gerada:", descricao)
