import requests

def get_referee_data(referee_id):
  url = "https://transfermarkt-db.p.rapidapi.com/v1/referees/profile"
  querystring = {"referee_id":{referee_id},"locale":"BR"}
  headers = { "x-rapidapi-key": "7b4ef99412msha2707ae4be4d7a4p15fc0ajsnf0cd1f224e20", "x-rapidapi-host": "transfermarkt-db.p.rapidapi.com" }
  response = requests.get(url, headers=headers, params=querystring)
  return response.json()