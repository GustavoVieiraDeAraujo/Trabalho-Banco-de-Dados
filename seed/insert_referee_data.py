from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_referee_data(referees_data):
  if not referees_data:
    print("Nenhum arbitro para inserir.")
    return
  query = """INSERT INTO Arbitro (id, apelido, nome, data_nascimento, nacionalidade, imagemURL, contrato_inicio) VALUES %s ON CONFLICT (id) DO NOTHING;"""
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, referees_data)
    conn.commit()
    print(f"{len(referees_data)} arbitros inseridos com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

# def prepare_referee_data(referee_data):
#   profile = referee_data.get("data", {}).get("profile", {})
#   data_nascimento = profile.get("dateOfBirth")
#   contrato_incio = profile.get("debut")
#   if data_nascimento == "0000-00-00" or not data_nascimento:
#     data_nascimento = None
#   if contrato_incio == "0000-00-00" or not contrato_incio:
#     contrato_incio = None
#   return (
#     int(profile["id"]),
#     profile.get("refereeName"),
#     f"{profile.get('firstName', '')} {profile.get('lastName', '')}".strip(),
#     data_nascimento,
#     translate_country(profile.get("countryName", "").encode("latin1").decode("utf-8")) or None,
#     profile.get("refereeImage") or None,
#     contrato_incio,
#   )