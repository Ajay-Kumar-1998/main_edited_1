import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG=False
    SQLITE_DB_DIR=None
    SQLALCHEMY_DATABASE_URI=None

class LocalDevelopementConfig(Config):
    SQLITE_DB_DIR=os.path.join(basedir,"../dataBase")
    SQLALCHEMY_DATABASE_URI="sqlite:///"+ os.path.join(SQLITE_DB_DIR,"final_project.sqlite3")
    DEBUG=True