import sqlite3
import hashlib

DB_PASSWORD = "admin123"

def get_user(username, user_input):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
