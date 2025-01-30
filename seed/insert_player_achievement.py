from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_player_achievement(player_achievements):
  if not player_achievements:
    print("Nenhum título para inserir.")
    return
  query = """INSERT INTO Titulo (nome) VALUES %sON CONFLICT DO NOTHING;"""
  values = [(title,) for title in player_achievements]
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, values)
    conn.commit()
    print(f"{len(values)} títulos inseridos com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()