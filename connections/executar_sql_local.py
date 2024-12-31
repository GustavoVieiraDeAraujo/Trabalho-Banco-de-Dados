import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("user_local")
HOST = os.getenv("host_local")
PORT = os.getenv("port_local")
DBNAME = os.getenv("dbname_local")
PASSWORD = os.getenv("password_local")

try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )

    print("Conexão bem sucedida")
    
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM sua_tabela;")
    
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
    
except Exception as e:
    print(f"Falha na conexão ou execução do sql {e}")