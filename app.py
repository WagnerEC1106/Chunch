from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from flask_softdelete import SoftDeleteMixin

app = Flask(__name__, static_folder='.', static_url_path='')

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# Serve your existing HTML pages
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    app.run(debug=True)

