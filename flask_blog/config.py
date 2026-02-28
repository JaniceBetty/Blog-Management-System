import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or 'sqlite:///site.db'
    ADMIN_CREATION_CODE = os.environ.get("ADMIN_CREATION_CODE")