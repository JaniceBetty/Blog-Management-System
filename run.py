import os
from dotenv import load_dotenv

load_dotenv()

from flask_blog import app, db

# Ensure tables exist on app startup, even with gunicorn
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)