import psycopg2

def connect_postgresql_database():
  return psycopg2.connect(
    dbname="futebol",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432",
    options="-c client_encoding=UTF8"
  )