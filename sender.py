import requests
from dotenv import load_dotenv
import os

load_dotenv()

instanceId = os.getenv("INSTANCE_ID")
token = os.getenv("TOKEN")
clientToken = os.getenv("CLIENT_TOKEN")


url = f"https://api.z-api.io/instances/{instanceId}/token/{token}/send-text"

def Mandar_msg(Numero,Nome):
    payload = {
        "phone": Numero,
        "message": f"Olá, {Nome} tudo bem com você?"
    }
    headers = {
        "Client-Token": clientToken,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    return(response.text)    