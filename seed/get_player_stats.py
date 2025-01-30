import requests

def get_player_stats(player_id):
  BASE_URL = f"https://transfermarkt-api.fly.dev/players/{player_id}/stats"
  response = requests.get(BASE_URL)
  if response.status_code == 200:
    try:
      return response.json()
    except ValueError:
      print(f"Erro ao decodificar JSON para o jogador {player_id}: {response.text}")
      return None
  else:
    print(f"Erro ao buscar estatísticas do jogador {player_id}: {response.status_code}")
    print(f"Resposta: {response.text}")
    return None