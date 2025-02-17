import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_coach_data(coach_id):
  url = "https://transfermarkt-db.p.rapidapi.com/v1/staff/profile"
  querystring = {"staff_id":{coach_id},"locale":"BR"}
  headers = { "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"), "x-rapidapi-host": "transfermarkt-db.p.rapidapi.com" }
  response = requests.get(url, headers=headers, params=querystring)
  return response.json()
