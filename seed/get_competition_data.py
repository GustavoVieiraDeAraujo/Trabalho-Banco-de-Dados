import requests

def get_competition_data(competition_id):
  url = "https://transfermarkt6.p.rapidapi.com/competitions/info"
  querystring = {"id":{competition_id},"domain":"com.br"}
  headers = { "x-rapidapi-key": "7b4ef99412msha2707ae4be4d7a4p15fc0ajsnf0cd1f224e20", "x-rapidapi-host": "transfermarkt6.p.rapidapi.com" }
  response = requests.get(url, headers=headers, params=querystring)
  return response.json()