from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database
from translate import translate_date, translate_city

def insert_coach_data(coach_data):
  query = """
    INSERT INTO Tecnico 
    (
      id, nome, apelido, data_nascimento, nacionalidade, imagemURL,
      contrato_inicio, contrato_fim, cidade_nascimento, id_time
    ) VALUES %s ON CONFLICT (id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    values = [prepare_coach_data(coach_data)]
    execute_values(cursor, query, values)
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

def prepare_coach_data(coach_data):
  profile = coach_data.get("data", {}).get("profile", {})
  functions = profile.get("functions", [{}])[0]
  return (
    int(profile["id"]),
    f"{profile.get('firstName', '')} {profile.get('lastName', '')}".strip(),
    profile.get("personName"),
    profile.get("dateOfBirth"),
    profile.get("countryName"),
    profile.get("personImage"),
    translate_date(functions.get("appointed", None)),
    translate_date(functions.get("contractUntil", None)),
    translate_city(profile.get("birthplace")),
    int(functions.get("clubID", 0)),
  )