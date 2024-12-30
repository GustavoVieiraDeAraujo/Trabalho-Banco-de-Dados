import requests

def get_club_data(club_id):
  url = f"https://transfermarkt-api.fly.dev/clubs/{club_id}/profile"
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    else:
      print(f"Erro na requisição: {response.status_code} - {response.text}")
      return None
  except Exception as e:
    print(f"Erro ao acessar a API: {e}")
    return None