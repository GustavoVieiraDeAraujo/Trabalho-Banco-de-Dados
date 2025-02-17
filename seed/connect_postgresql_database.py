import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_postgresql_database():
  return psycopg2.connect(
    dbname=os.getenv("DBNAME", "soccer"),
    user=os.getenv("DBUSER", "postgres"),
    password=os.getenv("DBPASSWORD"),
    host=os.getenv("DBHOST", "localhost"),
    port=os.getenv("DBPORT", "5432")
  )
