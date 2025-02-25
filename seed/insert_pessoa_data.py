from connect_postgresql_database import connect_postgresql_database

def insert_pessoa_data(id_pessoa, nome, apelido, data_nascimento, nacionalidade, imagemURL):
  query = """
    INSERT INTO Pessoa (id, nome, apelido, data_nascimento, nacionalidade, imagemURL)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """
  conn = connect_postgresql_database()
  cursor = conn.cursor()
  try:
    cursor.execute(query, (id_pessoa, nome, apelido, data_nascimento, nacionalidade, imagemURL))
    conn.commit()
  except Exception as e:
    print(f"Erro ao inserir pessoa: {e}")
    conn.rollback()
  finally:
    cursor.close()
    conn.close()
