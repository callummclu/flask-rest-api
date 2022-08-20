import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user="postgres",
    password="010305"
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS posts')

cur.execute('CREATE TABLE posts (id INTEGER PRIMARY KEY, title VARCHAR(255) NOT NULL, content TEXT)')

cur.execute('INSERT INTO posts (id,title, content) VALUES (%s,%s, %s)',(1,"title","content"))

conn.commit()

cur.close()
conn.close()