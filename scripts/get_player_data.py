import requests

def get_player_data(player_id):
  url = f"https://transfermarkt-api.fly.dev/players/{player_id}/profile"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Erro ao buscar dados: {response.status_code}")
    return None