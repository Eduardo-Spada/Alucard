import requests
import os

def get_image_description(image_path):
    # Defina a URL da API do Hugging Face ou qualquer outro serviço
    url = "https://api-inference.huggingface.co/models/Salesforce/blip2-opt-2.7b"
    
    # Envie a imagem para a API e receba a descrição
    headers = {
        "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
  # Substitua pelo seu token da API
    }

    # Abrir a imagem e enviar para a API
    with open(image_path, "rb") as img:
        response = requests.post(url, headers=headers, files={"file": img})

    # Verificar o retorno da API
    if response.status_code == 200:
        result = response.json()
        return result.get("description", "Descrição não disponível")
    else:
        return "Erro ao processar a imagem"
