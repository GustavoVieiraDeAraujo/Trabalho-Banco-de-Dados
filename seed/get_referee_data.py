import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_referee_data(referee_id):
  url = "https://transfermarkt-db.p.rapidapi.com/v1/referees/profile"
  querystring = {"referee_id":{referee_id},"locale":"BR"}
  headers = { "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"), "x-rapidapi-host": "transfermarkt-db.p.rapidapi.com" }
  response = requests.get(url, headers=headers, params=querystring)
  return response.json()
