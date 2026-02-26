import os
from dotenv import load_dotenv

load_dotenv()

from flask_blog import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)