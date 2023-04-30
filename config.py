import os
import secrets

# You need to set the environment variable
# $env:DATABASE_URI = "mysql+pymysql://user:password@localhost/dbname"

class Config:
    DEBUG = False
    TESTING = False
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    # Secret key for secure sessions
    SECRET_KEY = secrets.token_hex(16)