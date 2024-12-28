import requests

def get_players_id(clubs_id):
  players_id = []
  for club_id in clubs_id:
    players = get_players_by_club(club_id)
    players_id.extend(players)
  return players_id

def get_players_by_club(club_id):
  BASE_URL = "https://transfermarkt-api.fly.dev/clubs/{}/players"
  url = BASE_URL.format(club_id)
  response = requests.get(url)
  if response.status_code == 200:
    try:
      data = response.json()
      if "players" in data and isinstance(data["players"], list):
        return [player["id"] for player in data["players"]]
      else:
        print(f"Formato inesperado de dados para o clube {club_id}: {data}")
        return []
    except ValueError:
      print(f"Erro ao decodificar JSON para o clube {club_id}: {response.text}")
      return []
  else:
    print(f"Erro ao buscar jogadores do clube {club_id}: {response.status_code}")
    print(f"Resposta: {response.text}")
    return []