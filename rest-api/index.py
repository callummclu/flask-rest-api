import psycopg2 as db
from flask import Flask,request
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
        return "Created post"

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
    cur.execute("SELECT * FROM posts WHERE id ="+post_id)
    rows = cur.fetchone()
    cur.close()
    conn.close()

    post = {}
    post["post"] = rows

    return post

# Update one
@app.route('/<post_id>', methods=['PUT'])
def updateOne(post_id):

    postModel = request.json
    if not postModel:
        return "no post with id %s" % post_id, 400
    else:
        title = postModel['title']
        content = postModel['content']
        post = Post(title,content)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE posts SET title = %s, content = %s WHERE id = %s", (title, content, post_id))
        conn.commit()
        cur.close()
        conn.close()
        return "Edited post"


# Delete one
@app.route('/<post_id>', methods=['DELETE'])
def deleteOne(post_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM posts WHERE id = "+post_id)
    conn.commit()
    cur.close()
    conn.close()
    return "Deleted post"
