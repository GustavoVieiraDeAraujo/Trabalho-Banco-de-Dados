import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("user")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")
PASSWORD = os.getenv("password")

try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Conectado com banco de dados com sucesso")
    
    cursor = connection.cursor()
    
    query = "INSERT INTO Titulo (id, nome, ano) VALUES (%s, %s, %s)"
    values = (1, 'Teste', 2022)
    
    cursor.execute(query, values)
    connection.commit()
    
    cursor.close()
    connection.close()
    print("Conexão fechada")

except Exception as e:
    print(f"Falha na conexão ou execução do sql {e}")
