import requests

def get_matches_id(competitionId, seasonId):
  matches_id = []
  for i in range(1,39):
    url = "https://transfermarkt6.p.rapidapi.com/competitions/play-day-matches"
    querystring = {"id":{competitionId},"seasonId":{seasonId},"matchDay":{i},"domain":"com.br"}
    headers = {"x-rapidapi-key": "7b4ef99412msha2707ae4be4d7a4p15fc0ajsnf0cd1f224e20","x-rapidapi-host": "transfermarkt6.p.rapidapi.com"}
    response = requests.get(url, headers=headers, params=querystring)
    for j in range(0,10):
      matches_id.append(response.json()["data"]["playDayMatches"][j]["id"])
  return matches_id