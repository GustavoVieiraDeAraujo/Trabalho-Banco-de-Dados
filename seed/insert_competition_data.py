from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database
from translate import translate_country

def insert_competition_data(competition_data):
  query = """
    INSERT INTO Competicao
    (
      id, nome, ano, confederacao, imagemURL, divisao
    ) 
    VALUES %s ON CONFLICT (id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_competition_data(competition_data)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_competition_data(competition_data):
  competition = competition_data.get("data", {}).get("competition", {})
  return (
    competition["id"],
    competition.get("competitionName"),
    competition.get("season")-1,
    translate_country(competition.get("competitionCountryName", "").encode("latin1").decode("utf-8")) or None,
    competition.get("competitionImage") or None,
    competition.get("leagueLevel"),
  )