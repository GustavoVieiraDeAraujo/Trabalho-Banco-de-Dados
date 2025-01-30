from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_player_stats(player_stats_summary):
  if not player_stats_summary:
    print("Nenhuma estatistica para inserir.")
    return
  query = """INSERT INTO Estatistica (jogos, gols, assistencias, vermelhos, amarelos, minutos, id_jogador) VALUES %s ON CONFLICT DO NOTHING;"""
  values = [(
    player_stats_summary.get("Jogos", 0),
    player_stats_summary.get("Gols", 0),
    player_stats_summary.get("Assistências", 0),
    player_stats_summary.get("Cartões Vermelhos", 0),
    player_stats_summary.get("Cartões Amarelos", 0),
    player_stats_summary.get("Minutos Jogados", 0),
    player_stats_summary.get("idPlayer")
  )]
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, values)
    conn.commit()
    print(f"{len(values)} estatisticas inseridas com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()