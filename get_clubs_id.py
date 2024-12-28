import requests

def get_clubs_id(competition_id):
  BASE_URL = "https://transfermarkt-api.fly.dev/competitions/{}/clubs"
  url = BASE_URL.format(competition_id)
  try:
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      if "clubs" in data and isinstance(data["clubs"], list):
        clubs_id = [club['id'] for club in data["clubs"]]
        return clubs_id
      else:
        return "Nenhum clube encontrado para esta competição."
    else:
      return f"Erro na requisição: {response.status_code} - {response.text}"
  except Exception as e:
    return f"Erro ao acessar a API: {e}"