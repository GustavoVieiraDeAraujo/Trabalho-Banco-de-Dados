from connect_postgresql_database import connect_postgresql_database
from translate import translate_date, translate_city
from insert_pessoa_data import insert_pessoa_data

def insert_coach_data(coach_data):
  pessoa, tecnico = prepare_coach_data(coach_data)
  insert_pessoa_data(*pessoa)

  query = """
    INSERT INTO Tecnico (contrato_inicio, contrato_fim, cidade_nascimento, id_time, id_pessoa)
    VALUES (%s, %s, %s, %s, %s);
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    cursor.execute(query, tecnico)
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

  id_pessoa = int(profile["id"])
  club_id = functions.get("clubID")

  pessoa = (
    id_pessoa,
    f"{profile.get('firstName', '')} {profile.get('lastName', '')}".strip(),
    profile.get("personName"),
    profile.get("dateOfBirth"),
    profile.get("countryName"),
    profile.get("personImage"),
  )

  tecnico = (
    translate_date(functions.get("appointed")),
    translate_date(functions.get("contractUntil")),
    translate_city(profile.get("birthplace")),
    int(club_id) if club_id else None,
    id_pessoa,
  )

  return pessoa, tecnico
