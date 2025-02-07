import requests

def get_match_data(match_id):
  url = "https://transfermarkt6.p.rapidapi.com/fixtures/info"
  querystring = {"id":{match_id}}
  headers = {"x-rapidapi-key": "858da306e6mshdadcd289cbead99p135c26jsnc190725bbb08","x-rapidapi-host": "transfermarkt6.p.rapidapi.com"}
  response = requests.get(url, headers=headers, params=querystring)
  data = response.json()["data"]["gameInformation"]["dateSmall"]
  horario = response.json()["data"]["gameInformation"]["time"]
  publico = response.json()["data"]["gameInformation"]["spectators"]
  rodada = response.json()["data"]["gameInformation"]["competitionRound"]
  id_competicao = response.json()["data"]["gameInformation"]["competitionID"]
  id_estadio = response.json()["data"]["gameInformation"]["stadiumID"]
  id_arbitro = response.json()["data"]["gameInformation"]["refereeID"]
  url = "https://transfermarkt6.p.rapidapi.com/fixtures/result"
  response = requests.get(url, headers=headers, params=querystring)
  gols_mandante = response.json()["data"]["goalsHome"]
  gols_visitante = response.json()["data"]["goalsAway"]
  match_data ={"id": match_id, "data": data, "horario": horario, "publico": publico, "rodada": rodada, "id_competicao": id_competicao, "id_estadio": id_estadio, "id_arbitro": id_arbitro, "gols_mandante": gols_mandante, "gols_visitante": gols_visitante}
  return match_data