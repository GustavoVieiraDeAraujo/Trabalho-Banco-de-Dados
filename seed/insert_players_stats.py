from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_players_stats(players_stats):
  if not players_stats:
    print("Nenhuma estatistica para inserir.")
    return
  query = """INSERT INTO Estatistica (jogos, gols, assistencias, vermelhos, amarelos, minutos, id_jogador) VALUES %s ON CONFLICT DO NOTHING;"""
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, players_stats)
    conn.commit()
    print(f"{len(players_stats)} estatisticas inseridas com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()