from translate import translate_position, translate_country, translate_foot, translate_market_value, translate_height
from connect_postgresql_database import connect_postgresql_database
from insert_pessoa_data import insert_pessoa_data

def insert_player_data(player_data):
  pessoa = prepare_pessoa_data(player_data)
  insert_pessoa_data(*pessoa)

  query = """
    INSERT INTO Jogador
    (
      id, posicao, altura, pe_dominante, valor_mercado, cidade_nascimento,
      numero_camisa, agente, patrocinador, redes_sociais,
      contrato_incio, contrato_fim, id_time, id_pessoa
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    cursor.execute(query, prepare_player_data(player_data))
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_pessoa_data(player_data):
  place_of_birth = player_data.get("placeOfBirth", {})
  citizenship = player_data.get("citizenship") or []
  nacionalidade = citizenship[0] if citizenship else place_of_birth.get("country")
  return (
    int(player_data["id"]),
    player_data.get("fullName") or player_data.get("name"),
    player_data.get("name"),
    player_data.get("dateOfBirth"),
    translate_country(nacionalidade),
    player_data.get("imageUrl"),
  )

def prepare_player_data(player_data):
  place_of_birth = player_data.get("placeOfBirth", {})
  position = player_data.get("position", {})
  club = player_data.get("club", {})
  agent = player_data.get("agent") or {}

  shirt_number = player_data.get("shirtNumber")
  numero_camisa = int(str(shirt_number).replace("#", "")) if shirt_number else None

  club_id = club.get("id")

  return (
    int(player_data["id"]),
    translate_position(position.get("main")),
    translate_height(player_data.get("height")),
    translate_foot(player_data.get("foot")),
    translate_market_value(player_data.get("marketValue")),
    place_of_birth.get("city"),
    numero_camisa,
    agent.get("name"),
    player_data.get("outfitter").title() if player_data.get("outfitter") else None,
    next((link for link in (player_data.get("socialMedia") or []) if "instagram.com/" in link), None),
    club.get("joined"),
    club.get("contractExpires"),
    int(club_id) if club_id else None,
    int(player_data["id"]),
  )
