from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database
import requests

def insert_club_data(club_data):
  query = """
    INSERT INTO Time 
    (
      id, imagem_escudo, nome, apelido, data_fundacao, site_time_url,
      quantidade_socios, quantidade_jogadores_selecao, valor_mercado,
      id_estadio, id_localizacao
    ) 
    VALUES %s ON CONFLICT (id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_club_data(club_data, cursor)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def get_id_estadio(nome_estadio, cursor):
  query = "SELECT id FROM estadio WHERE nome = %s;"
  cursor.execute(query, (nome_estadio,))
  result = cursor.fetchone()
  return result[0] if result else None

def get_id_localizacao(nome_localizacao, cursor):
  query = "SELECT id FROM localizacao WHERE cidade = %s;"
  cursor.execute(query, (nome_localizacao,))
  result = cursor.fetchone()
  return result[0] if result else None

def prepare_club_data(club_data, cursor):
  squad = club_data.get("squad", {})
  imagem = club_data.get("image")
  response = requests.get(imagem)
  imagem_bytes = response.content
  address_line2 = club_data.get("addressLine2", "")
  cidade = None
  if address_line2:
    if "," in address_line2:
      cidade = address_line2.split(",")[0].strip().title()
    else:
      cidade = address_line2.partition(" ")[2].strip().title()
  return (
    int(club_data["id"]),
    imagem_bytes,
    club_data.get("officialName", ""),
    club_data.get("name", ""),
    club_data.get("foundedOn", ""),
    club_data.get("website", ""),
    int(club_data.get("members", "0"))*1000,
    int(squad.get("nationalTeamPlayers", "0")),
    club_data.get("currentMarketValue"),
    get_id_estadio(club_data.get("stadiumName"), cursor),
    get_id_localizacao(cidade, cursor)
  )