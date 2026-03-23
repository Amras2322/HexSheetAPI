import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

url = 'https://nmzkkypjourlffqrzpkq.supabase.co/functions/v1/api/v1/homebrew/spells'
headers = {
    'x-api-key': os.getenv("API_KEY"),
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()

with open('spells.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Spells saved to spells.json")
