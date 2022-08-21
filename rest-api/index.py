from json import JSONEncoder
import psycopg2 as db
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db_sql = SQLAlchemy(app)

class Post(db_sql.Model):
    id = db_sql.Column(db_sql.Integer, primary_key=True)
    title = db_sql.Column(db_sql.String(255))
    content = db_sql.Column(db_sql.String(255))

    def __init__(self,title,content):
        self.title = title
        self.content = content


def get_db_connection():
    conn = db.connect(
        host="localhost",
        database="flask_db",
        user="postgres",
        password="010305"
    )
    return conn

# Create one
@app.route('/', methods=['POST'])
def create():
    postModel = request.json
    if not postModel:
        return "No model to create", 400
    else:
        title = postModel['title']
        content = postModel['content']
        post = Post(title,content)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO posts (title,content) VALUES (%s,%s)", (post.title, post.content))
        conn.commit()
        cur.close()
        conn.close()
        return "Created"

# Read all
@app.route('/')
def getAll():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    posts = {}
    posts["posts"] = rows

    return posts

# Read One
@app.route('/<post_id>')
def getOne(post_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE id = %s", post_id)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    posts = {}
    posts["posts"] = rows

    return posts

# Update one

# Delete one
