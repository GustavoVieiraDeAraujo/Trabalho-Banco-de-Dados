import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_coaches_id(competition_id):
  url = "https://transfermarkt-db.p.rapidapi.com/v1/competitions/coaches"
  querystring = {"competition_id":{competition_id},"locale":"BR"}
  headers = { "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"), "x-rapidapi-host": "transfermarkt-db.p.rapidapi.com" }
  response = requests.get(url, headers=headers, params=querystring)
  data = response.json()
  coaches_id = [item['id'] for item in data['data'] if 'id' in item]
  return coaches_id
