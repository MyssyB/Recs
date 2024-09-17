#!/usr/bin/python3
""" User class"""

class User:
    def __init__(self, id, name, email, password)
    self.id = id # type: ignore
    self.name = name # type: ignore
    self.email = email # type: ignore
    self.password = password # type: ignore

def save_to_db(self):
    cursor = mysql.connection.cursor() # type: ignore
    cursor.execute("INSERT INTO users (name, email, password) VALUES(%s, %s, %s)", (self.name, self.email, self.password))
    mysql.connection.commit() # type: ignore
    cursor.close()