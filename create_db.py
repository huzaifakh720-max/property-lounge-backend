import sqlite3

conn = sqlite3.connect("properties.db")

cursor = conn.cursor()

# create properties table
cursor.execute("""
CREATE TABLE IF NOT EXISTS properties (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
price TEXT,
location TEXT,
image TEXT
)
""")

# create contacts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
message TEXT
)
""")

# insert sample properties
cursor.execute("""
INSERT INTO properties (title,price,location,image)
VALUES
('Luxury Apartment','₹1.2 Cr','Mumbai','property1.jpg'),
('Sea Facing Villa','₹3.5 Cr','Bandra','property2.jpg'),
""")

conn.commit()
conn.close()

print("Database and tables created successfully")


import sqlite3

conn = sqlite3.connect("properties.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE properties(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
price TEXT,
location TEXT,
image TEXT
)
""")

conn.commit()
conn.close()