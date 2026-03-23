import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://nmzkkypjourlffqrzpkq.supabase.co/functions/v1/api/v1/homebrew/spells'
headers = {
    'x-api-key': os.getenv("API_KEY"),
    'Content-Type': 'application/json'
}

payload = {
    "name": "Ice Knife",
    "index": "ice-knife",
    "level": 1,
    "school": "Conjuration",
    "casting_time": "1 Action",
    "ritual": False,
    "concentration": False,
    "range": "60 feet",
    "components": "M, S",
    "material": "A drop of water or a piece of ice",
    "duration": "Instantaneous",
    "description": "You create a shard of ice and fling it at one creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 Piercing damage. Hit or miss, the shard then explodes. The target and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 2d6 Cold damage.",
    "higher_levels": "The Cold damage increases by 1d6 for each spell slot level above 1.",
    "ruleset": "2024",
    "classes": [
                {
                    "name": "druid",
                    "index": "druid"
                },
                {
                    "name": "wizard",
                    "index": "wizard"
                },
                {
                    "name": "sorcerer",
                    "index": "sorcerer"
                }
            ],
    "is_public": True
}
response = requests.post(url, headers=headers, json=payload)
data = response.json()
print(data)