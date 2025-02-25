import requests
from connect_postgresql_database import connect_postgresql_database
from translate import translate_country, translate_market_value

def insert_club_data(club_data):
  id_localizacao = insert_localizacao_data(club_data)
  id_estadio = insert_estadio_data(club_data, id_localizacao)
  insert_time_data(club_data, id_estadio, id_localizacao)

def insert_localizacao_data(club_data):
  cidade = club_data.get("addressLine2").partition(" ")[2] if club_data.get("addressLine2") else None
  pais = translate_country(club_data.get("addressLine3"))

  query = """
    INSERT INTO Localizacao (pais, cidade)
    VALUES (%s, %s)
    RETURNING id;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    cursor.execute(query, (pais, cidade))
    id_localizacao = cursor.fetchone()[0]
    conn.commit()
    return id_localizacao
  except Exception as e:
    print(f"Erro ao inserir localizacao: {e}")
    conn.rollback()
    return None
  finally:
    cursor.close()
    conn.close()

def insert_estadio_data(club_data, id_localizacao):
  query = """
    INSERT INTO Estadio (nome, capacidade_pessoas, id_localizacao)
    VALUES (%s, %s, %s)
    RETURNING id;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    cursor.execute(query, (
      club_data.get("stadiumName"),
      club_data.get("stadiumSeats"),
      id_localizacao,
    ))
    id_estadio = cursor.fetchone()[0]
    conn.commit()
    return id_estadio
  except Exception as e:
    print(f"Erro ao inserir estadio: {e}")
    conn.rollback()
    return None
  finally:
    cursor.close()
    conn.close()

def download_escudo(image_url):
  # Requisito da disciplina: pelo menos uma coluna com dado binario (BYTEA).
  if not image_url:
    return None
  try:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; trabalho-banco-de-dados/1.0)"}
    response = requests.get(image_url, headers=headers, timeout=10)
    if response.status_code == 200:
      return response.content
  except Exception as e:
    print(f"Erro ao baixar o escudo do time: {e}")
  return None

def insert_time_data(club_data, id_estadio, id_localizacao):
  squad = club_data.get("squad") or {}

  query = """
    INSERT INTO Time
    (
      id, imagem_escudo, nome, apelido, data_fundacao, site_time_url,
      quantidade_socios, quantidade_jogadores_selecao, valor_mercado,
      id_estadio, id_localizacao
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    cursor.execute(query, (
      int(club_data["id"]),
      download_escudo(club_data.get("image")),
      club_data.get("officialName") or club_data.get("name"),
      club_data.get("name"),
      club_data.get("foundedOn"),
      club_data.get("website"),
      club_data.get("members"),
      squad.get("nationalTeamPlayers"),
      translate_market_value(club_data.get("currentMarketValue")),
      id_estadio,
      id_localizacao,
    ))
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados do time: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()
