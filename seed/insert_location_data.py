from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_location_data(location_data):
  if not location_data: 
    print("Nenhuma localizacao para inserir.")
    return
  query = """INSERT INTO Localizacao(pais, regiao, estado, cidade) VALUES %s ON CONFLICT DO NOTHING;"""
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, location_data)
    conn.commit()
    print(f"{len(location_data)} localizacoes inseridos com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

# def prepare_location_data(location):
#   state, region = get_region_and_state(location)
#   return (
#     "Brasil",
#     region,
#     state,
#     location
#   )