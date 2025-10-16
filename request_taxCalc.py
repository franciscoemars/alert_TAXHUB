import requests
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
#TAXHUB_URL=http://ip:8189/atosdata/TaxCalc
#TAXHUB_AUTHORIZATION=Basic 
load_dotenv()

def consumir_taxhub():
    url = os.environ['TAXHUB_URL']
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.environ['TAXHUB_AUTHORIZATION']
    }
    payload = {
        "items": [
            {"id": "0"}
        ],
        "shippingDestination": {
            "state": "SP"
        },
        "orderFormId": "a09db86448e24c2e9aa086fac8b9fa28",
        "salesChannel": "1"
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

# Exemplo de uso
#if __name__ == "__main__":
#    resposta = consumir_taxhub()
#    print(resposta)