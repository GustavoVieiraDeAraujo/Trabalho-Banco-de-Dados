from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_competition_data(competitions_data):
  if not competitions_data:
    print("Nenhuma competicao para inserir")
    return
  query = """INSERT INTO Competicao(id, nome, ano, confederacao, quantidade_times) VALUES %s ON CONFLICT (id) DO NOTHING;"""
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, competitions_data)
    conn.commit()
    print(f"{len(competitions_data)} competicoes inseridos com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

# def prepare_competition_data(competition_data):
#   competition = competition_data.get("data", {}).get("competition", {})
#   return (
#     competition["id"],
#     competition.get("competitionName"),
#     competition.get("season")-1,
#     translate_country(competition.get("competitionCountryName", "").encode("latin1").decode("utf-8")) or None,
#     competition.get("competitionImage") or None,
#     competition.get("leagueLevel"),
#   )