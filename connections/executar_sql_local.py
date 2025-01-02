import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("user_local")
HOST = os.getenv("host_local")
PORT = os.getenv("port_local")
DBNAME = os.getenv("dbname_local")
PASSWORD = os.getenv("password_local")

# Caminho para a imagem do escudo
caminho_imagem = './assets/estrela.jpg'

# Dados do time
nome_time = "TimeTeste1"
apelido_time = "TT1"
data_fundacao = "2000-01-01"
cores = "Azul e Branco"
quantidade_jogadores = 999
site_time_url = "http://www.time.com"
quantidade_socios = 999
idade_media_jogadores = 999
quantidade_jogadores_estrangeiros = 999
quantidade_jogadores_selecao = 999
id_estadio = 1

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

    with open(caminho_imagem, 'rb') as f:
        imagem_binaria = f.read()

    insert_query = """
    INSERT INTO Time (
        imagem_escudo, nome, apelido, data_fundacao, cores,
        quantidade_jogadores, site_time_url, quantidade_socios, 
        idade_media_jogadores, quantidade_jogadores_estrangeiros,
        quantidade_jogadores_selecao, id_estadio
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    cursor.execute(insert_query, (
        imagem_binaria, nome_time, apelido_time, data_fundacao, cores,
        quantidade_jogadores, site_time_url, quantidade_socios, idade_media_jogadores,
        quantidade_jogadores_estrangeiros, quantidade_jogadores_selecao, id_estadio
    ))

    connection.commit()

    print("Imagem e dados do time inseridos com sucesso!")

    cursor.close()
    connection.close()

except Exception as e:
    print(f"Falha na conexão ou execução do SQL: {e}")
