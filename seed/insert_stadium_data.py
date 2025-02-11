from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database
import re

def insert_stadium_data(estadios):
  if not estadios:
    print("Nenhum estadio para inserir.")
    return
  query = """INSERT INTO Estadio(id, data_fundacao, nome, capacidade_pessoas, id_localizacao) VALUES %s ON CONFLICT (id) DO NOTHING;"""
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, estadios)
    conn.commit()
    print(f"{len(estadios)} estadios inseridos com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

# def get_location_id(city_name):
#   conn = connect_postgresql_database()
#   cursor = conn.cursor()
#   try:
#     query = "SELECT id FROM Localizacao WHERE cidade = %s LIMIT 1;"
#     cursor.execute(query, (city_name,))
#     result = cursor.fetchone()
#     return result[0] if result else None
#   except Exception as e:
#     print(f"Erro ao buscar localização: {e}")
#     return None
#   finally:
#     cursor.close()
#     conn.close()

# def prepare_stadium_data(stadium):
#   stadium["city"] = re.sub(r"\s*\(.*?\)", "", stadium["city"]).strip()
#   return (
#     int(stadium["id"]),
#     stadium["constructionYear"],
#     stadium["name"],
#     stadium["totalCapacity"],
#     get_location_id(stadium["city"]),
#   )