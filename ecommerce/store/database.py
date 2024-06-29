# app/database.py
import psycopg2

# Function to create a table in PostgreSQL
def create_table():
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host='db'
    )
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert records into the database
def insert_records(name):
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host='db'
    )
    cur = conn.cursor()
    cur.execute('INSERT INTO records (name) VALUES (%s)', (name,))
    conn.commit()
    conn.close()

# Function to fetch records from the database
def fetch_records():
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host='db'
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM records')
    records = cur.fetchall()
    conn.close()
    return records
