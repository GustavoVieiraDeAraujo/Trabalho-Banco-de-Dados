from psycopg2.extras import execute_values
from connect_postgresql_database import connect_postgresql_database

def insert_coach_data(coaches_data):
  if not coaches_data:
    print("Nenhum técnico para inserir.")
    return
  query = """INSERT INTO Tecnico (id, nome, apelido, data_nascimento, nacionalidade, imagemURL,contrato_inicio, contrato_fim, cidade_nascimento, id_time) VALUES %s ON CONFLICT (id) DO NOTHING;"""
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    execute_values(cursor, query, coaches_data)
    conn.commit()
    print(f"{len(coaches_data)} tecnicos inseridos com sucesso!")
  except Exception as e:
    print(f"Erro ao inserir dados: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()

# def prepare_coach_data(coach_data):
#   profile = coach_data.get("data", {}).get("profile", {})
#   functions = profile.get("functions", [{}])[0]
#   return (
#     int(profile["id"]),
#     f"{profile.get('firstName', '')} {profile.get('lastName', '')}".strip(),
#     profile.get("personName"),
#     profile.get("dateOfBirth"),
#     profile.get("countryName"),
#     profile.get("personImage"),
#     translate_date(functions.get("appointed", None)),
#     translate_date(functions.get("contractUntil", None)),
#     translate_city(profile.get("birthplace")),
#     int(functions.get("clubID", 0)),
#   )