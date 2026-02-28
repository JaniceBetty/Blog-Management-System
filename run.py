import os
from dotenv import load_dotenv

load_dotenv(override=True)  # Load environment variables from .env file, allowing overrides

from flask_blog import app, db

# Ensure tables exist on app startup, even with gunicorn
with app.app_context():
    db.create_all()

print("Tables created successfully!")

if __name__ == "__main__":
    app.run(debug=True)