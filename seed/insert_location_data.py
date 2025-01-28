from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database
from translate import get_region_and_state

def insert_location_data(location):
  query = """
    INSERT INTO Localizacao
    (
      pais, regiao, estado, cidade
    ) 
    VALUES %s ON CONFLICT DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_location_data(location)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_location_data(location):
  state, region = get_region_and_state(location)
  return (
    "Brasil",
    region,
    state,
    location
  )