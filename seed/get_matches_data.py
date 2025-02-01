import requests

def get_matches_data(matches_id):
  matches_data = []
  for i in range(0, len(matches_id)):
    url = "https://transfermarkt6.p.rapidapi.com/fixtures/info"
    querystring = {"id":{matches_id[i]}}
    headers = {"x-rapidapi-key": "7b4ef99412msha2707ae4be4d7a4p15fc0ajsnf0cd1f224e20","x-rapidapi-host": "transfermarkt6.p.rapidapi.com"}
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
    match_data ={"id": matches_id[i], "data": data, "horario": horario, "publico": publico, "rodada": rodada, "id_competicao": id_competicao, "id_estadio": id_estadio, "id_arbitro": id_arbitro, "gols_mandante": gols_mandante, "gols_visitante": gols_visitante}
    matches_data.append(match_data)
  return matches_data