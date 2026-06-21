from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "database/doccollab.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        owner TEXT,
        created_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS comments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        comment TEXT,
        created_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS versions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        version_no INTEGER,
        content TEXT,
        created_at TEXT
    )
    """)

    conn.commit()

    count = cur.execute(
        "SELECT COUNT(*) as total FROM documents"
    ).fetchone()

    if count["total"] == 0:

        cur.execute("""
        INSERT INTO documents
        (title, content, owner, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            "ParkingIQ Smart Parking Cloud",
            "Cloud Parking Management System",
            "Vrish Thadani",
            datetime.now().strftime("%d-%m-%Y")
        ))

        conn.commit()

    conn.close()


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    conn = get_db()

    documents = conn.execute("""
    SELECT *
    FROM documents
    ORDER BY id DESC
    """).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        documents=documents
    )


@app.route("/editor")
def editor():

    conn = get_db()

    document = conn.execute("""
    SELECT *
    FROM documents
    LIMIT 1
    """).fetchone()

    comments = conn.execute("""
    SELECT *
    FROM comments
    ORDER BY id DESC
    """).fetchall()

    version_count = conn.execute("""
    SELECT COUNT(*) as total
    FROM versions
    """).fetchone()["total"]

    conn.close()

    return render_template(
        "editor.html",
        document=document,
        comments=comments,
        version_count=version_count
    )


@app.route("/comments")
def comments():

    conn = get_db()

    comments = conn.execute("""
    SELECT *
    FROM comments
    ORDER BY id DESC
    """).fetchall()

    conn.close()

    return render_template(
        "comments.html",
        comments=comments
    )


@app.route("/versions")
def versions():

    conn = get_db()

    versions = conn.execute("""
    SELECT *
    FROM versions
    ORDER BY id DESC
    """).fetchall()

    conn.close()

    return render_template(
        "versions.html",
        versions=versions
    )


@app.route("/architecture")
def architecture():
    return render_template("architecture.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/conflict")
def conflict():
    return render_template("conflicts.html")


@app.route("/analytics")
def analytics():

    conn = get_db()

    documents = conn.execute(
        "SELECT COUNT(*) as total FROM documents"
    ).fetchone()["total"]

    comments = conn.execute(
        "SELECT COUNT(*) as total FROM comments"
    ).fetchone()["total"]

    versions = conn.execute(
        "SELECT COUNT(*) as total FROM versions"
    ).fetchone()["total"]

    collaborators = 4

    conn.close()

    return render_template(
        "analytics.html",
        documents=documents,
        comments=comments,
        versions=versions,
        collaborators=collaborators
    )


@app.route("/add-comment", methods=["POST"])
def add_comment():

    username = request.form.get("username")
    comment = request.form.get("comment")

    if not username or not comment:
        return jsonify({
            "status": "error"
        })

    conn = get_db()

    conn.execute("""
    INSERT INTO comments
    (username, comment, created_at)
    VALUES (?, ?, ?)
    """,
    (
        username,
        comment,
        datetime.now().strftime("%d-%m-%Y %H:%M")
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "status": "success"
    })


@app.route("/save-document", methods=["POST"])
def save_document():

    content = request.form.get("content")

    if not content:
        return jsonify({
            "status": "error"
        })

    conn = get_db()

    count = conn.execute("""
    SELECT COUNT(*) as total
    FROM versions
    """).fetchone()

    version_no = count["total"] + 1

    conn.execute("""
    INSERT INTO versions
    (version_no, content, created_at)
    VALUES (?, ?, ?)
    """,
    (
        version_no,
        content,
        datetime.now().strftime("%d-%m-%Y %H:%M")
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "status": "saved",
        "version": version_no
    })


if __name__ == "__main__":
    init_db()
    app.run(debug=True)