import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

def get_connection():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password = "734845709",
        database = "signup_db"
    )