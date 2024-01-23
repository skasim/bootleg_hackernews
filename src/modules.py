import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

# initializing the app
app = Flask(__name__)
app.debug = True

# Configs
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://samra:@{os.getenv('PSQL_HOST')}:5432/hackernews"
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True 

db = SQLAlchemy(app)