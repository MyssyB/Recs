#!/usr/bin.python3
"""Configuration file for setting up flask and mysql"""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/recs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
