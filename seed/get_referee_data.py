import requests

def get_referee_data(referee_id):
  url = "https://transfermarkt6.p.rapidapi.com/referees/profile"
  querystring = {"id":{referee_id},"domain":"com.br"}
  headers = { "x-rapidapi-key": "071fe47769mshcb7d822bf1bd8bap1c6fabjsnabf89307db52", "x-rapidapi-host": "transfermarkt6.p.rapidapi.com" }
  response = requests.get(url, headers=headers, params=querystring)
  return response.json()