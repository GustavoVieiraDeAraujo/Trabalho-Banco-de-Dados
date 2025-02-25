from connect_postgresql_database import connect_postgresql_database
from translate import translate_country
from insert_pessoa_data import insert_pessoa_data

def insert_referee_data(referee_data):
  pessoa, arbitro = prepare_referee_data(referee_data)
  insert_pessoa_data(*pessoa)

  query = """
    INSERT INTO Arbitro (contrato_inicio, id_pessoa)
    VALUES (%s, %s);
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    cursor.execute(query, arbitro)
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
  if date_of_birth == "0000-00-00" or not date_of_birth:
    date_of_birth = None
  if debut_date == "0000-00-00" or not debut_date:
    debut_date = None

  id_pessoa = int(profile["id"])

  pessoa = (
    id_pessoa,
    f"{profile.get('firstName', '')} {profile.get('lastName', '')}".strip(),
    profile.get("refereeName"),
    date_of_birth,
    translate_country(profile.get("countryName")) or None,
    profile.get("refereeImage") or None,
  )

  # Arbitro.contrato_inicio e INT (guarda so o ano de estreia na liga).
  contrato_inicio = int(debut_date[:4]) if debut_date else None

  arbitro = (
    contrato_inicio,
    id_pessoa,
  )

  return pessoa, arbitro
