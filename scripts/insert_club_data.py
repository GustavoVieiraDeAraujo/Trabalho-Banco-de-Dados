from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database
from translate import translate_country, translate_market_value

def insert_club_data(club_data):
  query = """
    INSERT INTO clubs 
    (
      team_id, shortName, fullName, imageURL, city, country, website,
      dateOfFoundation, members, marketValue, squadSize, squadAvarageAge,
      squadForeigners, squadNationalTeamPlayers, stadiumName, stadiumSeats, competition
    ) 
    VALUES %s ON CONFLICT (team_id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_club_data(club_data)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_club_data(club_data):
  squad = club_data.get("squad", {})
  league = club_data.get("league", {})
  return (
    int(club_data["id"]),
    club_data.get("name"),
    club_data.get("officialName"),
    club_data.get("image"),
    club_data.get("addressLine2").partition(" ")[2] if club_data.get("addressLine2") else None,
    translate_country(club_data.get("addressLine3", None)),
    club_data.get("website"),
    club_data.get("foundedOn"),
    club_data.get("members"),
    translate_market_value(club_data.get("currentMarketValue")),
    int(squad.get("size","0")),
    float(squad.get("averageAge", "0.0")),
    int(squad.get("foreigners", "0")),
    int(squad.get("nationalTeamPlayers", "0")),
    club_data.get("stadiumName"),
    club_data.get("stadiumSeats"),
    league.get("id", 0)
  )