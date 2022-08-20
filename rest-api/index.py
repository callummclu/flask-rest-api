from json import JSONEncoder
import os
import psycopg2 as db
from flask import Flask
app = Flask(__name__)

def get_db_connection():
    conn = db.connect(
        host="localhost",
        database="flask_db",
        user="postgres",
        password="010305"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    posts = {}
    posts["posts"] = rows

    return posts
