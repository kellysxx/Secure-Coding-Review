"""Intentionally vulnerable baseline for a local secure-coding review exercise."""
import sqlite3

def find_user(name):
    connection = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return connection.execute(query).fetchall()
