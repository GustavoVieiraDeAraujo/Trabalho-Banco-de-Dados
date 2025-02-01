from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_match_data(match_data):
  query = """
    INSERT INTO Jogo 
    (
      id, data, horario, publico, rodada, 
      gols_mandante, gols_visitante, id_competicao, id_estadio, id_arbitro
    ) 
    VALUES %s ON CONFLICT (id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_match_data(match_data)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_match_data(match_data):
  return (
    int(match_data['id']),
    match_data['data'],
    match_data['horario'],
    int(match_data['publico']),
    int(match_data['rodada'].split('.')[0]),
    int(match_data['gols_mandante']),
    int(match_data['gols_visitante']),
    match_data['id_competicao'],
    int(match_data['id_estadio']),
    int(match_data['id_arbitro']),
  )