import sqlite3

def get_db():
    conn = sqlite3.connect('weather_service.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    with open('schema_db.sql', 'r') as f:
        db.executescript(f.read())
    db.commit()