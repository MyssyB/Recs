import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    