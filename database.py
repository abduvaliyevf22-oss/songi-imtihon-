
import sqlite3

db = sqlite3.connect("imtihon.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sevimli_kinolar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nomi TEXT,
    top_kinolar TEXT,
    janrlar TEXT,
    vaqt INTEGER,
    tavsiya_etilgan TEXT
)
""")

db.commit()



