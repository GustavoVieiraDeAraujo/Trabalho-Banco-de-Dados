import requests

def get_coach_data(coach_id):
  url = "https://transfermarkt-db.p.rapidapi.com/v1/staff/profile"
  querystring = {"staff_id":{coach_id},"locale":"BR"}
  headers = { "x-rapidapi-key": "7b4ef99412msha2707ae4be4d7a4p15fc0ajsnf0cd1f224e20", "x-rapidapi-host": "transfermarkt-db.p.rapidapi.com" }
  response = requests.get(url, headers=headers, params=querystring)
  return response.json()