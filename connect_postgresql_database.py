import psycopg2

def connect_postgresql_database():
  return psycopg2.connect(
    dbname="soccer",
    user="postgres",
    password="17052003Lipe!",
    host="localhost",
    port="5432"
  )