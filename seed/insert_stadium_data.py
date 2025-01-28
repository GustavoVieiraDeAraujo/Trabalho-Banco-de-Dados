from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database
from translate import get_location_id

def insert_stadium_data(stadium):
  query = """
    INSERT INTO Estadio
    (
      id, data_fundacao, nome, capacidade, id_localizacao
    ) 
    VALUES %s ON CONFLICT (id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_stadium_data(stadium)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_stadium_data(stadium):
  return (
    int(stadium["id"]),
    stadium["constructionYear"],
    stadium["name"],
    stadium["totalCapacity"],
    get_location_id(stadium["city"].split("(")[0].strip()),
  )