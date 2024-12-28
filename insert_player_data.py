from psycopg2.extras import execute_values
from translate import translate_position, translate_country, translate_foot, translate_market_value
from connect_postgresql_database import connect_postgresql_database

def insert_player_data(player_data):
  query = """
    INSERT INTO players 
    (
      player_id, player_position, shortName, fullName, club, joinedClub, 
      contractExpires, dateOfBirth, countryOfBirth, cityOfBirth, age, 
      height, marketValue, imageURL, foot, shirtNumber, 
      agent, outfitter, socialMedia
    ) 
    VALUES %s ON CONFLICT (player_id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_player_data(player_data)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_player_data(player_data):
  place_of_birth = player_data.get("placeOfBirth", {})
  position = player_data.get("position", {})
  club = player_data.get("club", {})
  agent = player_data.get("agent", {})
  return (
    int(player_data["id"]),
    translate_position(position.get("main")),
    player_data.get("name"),
    player_data.get("nameInHomeCountry", player_data.get("fullName")),
    int(club.get("id", 0)),
    club.get("joined"),
    club.get("contractExpires"),
    player_data.get("dateOfBirth"),
    translate_country(place_of_birth.get("country")),
    place_of_birth.get("city"),
    int(player_data.get("age", 0)),
    player_data.get("height").replace(',', '.').replace('m', '').strip(),
    translate_market_value(player_data.get("marketValue")),
    player_data.get("imageURL"),
    translate_foot(player_data.get("foot")),
    int(player_data.get("shirtNumber", "0").replace("#", "")),
    agent.get("name"),
    player_data.get("outfitter").title() if player_data.get("outfitter") else None,
    next((link for link in player_data.get("socialMedia", []) if "http://www.instagram.com/" in link), None)
  )