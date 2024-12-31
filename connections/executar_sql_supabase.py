import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("user_supabase")
HOST = os.getenv("host_supabase")
PORT = os.getenv("port_supabase")
DBNAME = os.getenv("dbname_supabase")
PASSWORD = os.getenv("password_supabase")

try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    
    cursor = connection.cursor()
    
    query = "INSERT INTO Titulo (id, nome, ano) VALUES (%s, %s, %s)"
    values = (1, 'Teste', 2022)
    
    cursor.execute(query, values)
    connection.commit()
    
    cursor.close()
    connection.close()

except Exception as e:
    print(f"Falha na conexão ou execução do sql {e}")
