import requests

def get_players_achievements(clubs_id):
  achievements = set()
  for club_id in clubs_id:
    players_ids = get_players_by_club(club_id)
    for player_id in players_ids:
      player_achievements = get_achievements_by_player(player_id)
      achievements.update(player_achievements)
  return achievements

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

def get_achievements_by_player(player_id):
  BASE_URL = "https://transfermarkt-api.fly.dev/players/{}/achievements"
  url = BASE_URL.format(player_id)
  response = requests.get(url)
  if response.status_code == 200:
    try:
      data = response.json()
      if "achievements" in data and isinstance(data["achievements"], list):
        return [achievement["title"] for achievement in data["achievements"]]
      else:
        print(f"Formato inesperado de dados para o jogador {player_id}: {data}")
        return []
    except ValueError:
      print(f"Erro ao decodificar JSON para o jogador {player_id}: {response.text}")
      return []
  else:
    print(f"Erro ao buscar títulos do jogador {player_id}: {response.status_code}")
    print(f"Resposta: {response.text}")
    return []