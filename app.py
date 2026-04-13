print("THIS IS MY REAL APP RUNNING")
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# DATABASE CONNECTION
def get_db():
    conn = sqlite3.connect("properties.db")
    conn.row_factory = sqlite3.Row
    return conn

# CREATE DATABASE
def init_db():
    conn = sqlite3.connect("properties.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS properties(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT,
        location TEXT,
        image TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()

# INSERT SAMPLE DATA
def add_sample_data():
    conn = sqlite3.connect("properties.db")
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM properties").fetchall()

    if len(data) == 0:
        cursor.execute("""
        INSERT INTO properties(title,price,location,image)
        VALUES('Luxury Apartment','₹1.2 Cr','Mumbai','property1.jpg')
        """)

        cursor.execute("""
        INSERT INTO properties(title,price,location,image)
        VALUES('Sea View Villa','₹3.5 Cr','Goa','property2.jpg')
        """)

        cursor.execute("""
        INSERT INTO properties(title,price,location,image)
        VALUES('Modern Penthouse','₹2.1 Cr','Delhi','property3.jpg')
        """)

    conn.commit()
    conn.close()

# INIT
init_db()
add_sample_data()

# HOME PAGE
@app.route("/")
def home():
    db = get_db()
    location = request.args.get("location")

    if location:
        properties = db.execute(
            "SELECT * FROM properties WHERE location LIKE ?",
            ("%" + location + "%",)
        ).fetchall()
    else:
        properties = db.execute("SELECT * FROM properties").fetchall()

    return render_template("index.html", properties=properties)

# PROPERTY DETAIL
@app.route("/property/<int:id>")
def property_detail(id):
    db = get_db()
    property = db.execute(
        "SELECT * FROM properties WHERE id=?",
        (id,)
    ).fetchone()

    return render_template("property.html", property=property)

# ABOUT
@app.route("/about")
def about():
    return render_template("about.html")

# SERVICES
@app.route("/services")
def services():
    return render_template("services.html")

# PRIVACY
@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

# CONTACT
@app.route("/contact", methods=["GET", "POST"])
def contact():
    success = False

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        db = get_db()
        db.execute(
            "INSERT INTO contacts(name,email,message) VALUES(?,?,?)",
            (name, email, message)
        )
        db.commit()

        success = True

    return render_template("contact.html", success=success)

# VIEW MESSAGES
@app.route("/messages")
def messages():
    db = get_db()
    messages = db.execute("SELECT * FROM contacts").fetchall()
    return render_template("messages.html", messages=messages)

# RUN SERVER
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)