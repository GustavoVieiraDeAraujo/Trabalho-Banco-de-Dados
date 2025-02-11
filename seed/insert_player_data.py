from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_player_data(players_data):
  if not players_data:
    print("Nenhum jogador para inserir.")
    return
  query = """INSERT INTO Jogador (id, nome, apelido, data_nascimento, nacionalidade, imagem, posicao, altura, pe_dominante, valor_mercado, cidade_nascimento, numero_camisa, agente, patrocinador, redes_sociais, data_inicio_contrato, data_fim_contrato, id_time) VALUES %s ON CONFLICT (id) DO NOTHING;"""
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, players_data)
    conn.commit()
    print(f"{len(players_data)} jogadores inseridos com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

# def prepare_player_data(player_data):
#   place_of_birth = player_data.get("placeOfBirth", {})
#   position = player_data.get("position", {})
#   club = player_data.get("club", {})
#   agent = player_data.get("agent", {})
#   return (
#     int(player_data["id"]),
#     player_data.get("nameInHomeCountry", player_data.get("fullName")),
#     player_data.get("name"),
#     player_data.get("dateOfBirth"),
#     translate_country(place_of_birth.get("country")),
#     player_data.get("imageURL"),
#     translate_position(position.get("main")),
#     str(player_data.get("height", "")).replace(',', '.').replace('m', '').strip(),
#     translate_foot(player_data.get("foot")),
#     player_data.get("marketValue"),
#     place_of_birth.get("city"),
#     int(player_data.get("shirtNumber", "0").replace("#", "")),
#     agent.get("name"),
#     player_data.get("outfitter").title() if player_data.get("outfitter") else None,
#     next((link for link in player_data.get("socialMedia", []) if "http://www.instagram.com/" in link), None),
#     club.get("joined"),
#     club.get("contractExpires"),
#     int(club.get("id", 0)),
#   )