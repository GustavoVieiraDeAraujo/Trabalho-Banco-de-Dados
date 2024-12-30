from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database
from translate import translate_country

def insert_referee_data(referee_data):
  query = """
    INSERT INTO referees
    (
      referee_id, shortName, fullName, dateOfBirth, 
      age, countryOfBirth, joinedLeague, imageURL
    ) 
    VALUES %s ON CONFLICT (referee_id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_referee_data(referee_data)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_referee_data(referee_data):
  profile = referee_data.get("data", {}).get("profile", {})
  date_of_birth = profile.get("dateOfBirth")
  debut_date = profile.get("debut")
  age = profile.get("age")
  if date_of_birth == "0000-00-00" or not date_of_birth:
    date_of_birth = None
    age = None
  if debut_date == "0000-00-00" or not debut_date:
    debut_date = None
  return (
    int(profile["id"]),
    profile.get("refereeName"),
    f"{profile.get('firstName', '')} {profile.get('lastName', '')}".strip(),
    date_of_birth,
    age,
    translate_country(profile.get("countryName")) or None,
    debut_date,
    profile.get("refereeImage") or None,
  )