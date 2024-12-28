import requests

def get_competition_id(competition_name):
  BASE_URL = "https://transfermarkt-api.fly.dev/competitions/search/{}"
  url = BASE_URL.format(competition_name)
  try:
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      if "results" in data and isinstance(data["results"], list) and data["results"]:
        return data["results"][0]['id']
      else:
        return "Nenhuma competição encontrada."
    else:
      return f"Erro na requisição: {response.status_code} - {response.text}"
  except Exception as e:
    return f"Erro ao acessar a API: {e}"