import requests

def get_coaches_id(competition_id):
  url = "https://transfermarkt-db.p.rapidapi.com/v1/competitions/coaches"
  querystring = {"competition_id":{competition_id},"locale":"BR"}
  headers = { "x-rapidapi-key": "7b4ef99412msha2707ae4be4d7a4p15fc0ajsnf0cd1f224e20", "x-rapidapi-host": "transfermarkt-db.p.rapidapi.com" }
  response = requests.get(url, headers=headers, params=querystring)
  data = response.json()
  coaches_id = [item['id'] for item in data['data'] if 'id' in item]
  return coaches_id