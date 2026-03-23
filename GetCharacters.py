import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://nmzkkypjourlffqrzpkq.supabase.co/functions/v1/api/v1/characters"
headers = {
    "x-api-key": os.getenv("API_KEY")
}
response = requests.get(url, headers=headers)
print(response.json())
