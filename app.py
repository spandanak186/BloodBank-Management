from flask import Flask
from models.db import create_tables
from routes.auth import auth_bp
from routes.donor import donor_bp
from routes.search import search_bp

app = Flask(__name__)
app.config.from_pyfile("config.py")

create_tables()

app.register_blueprint(auth_bp)
app.register_blueprint(donor_bp)
app.register_blueprint(search_bp)

@app.route('/')
def home():
    return "<h1>Blood Bank System Running</h1><a href='/login'>Login</a>"

if __name__ == "__main__":
    app.run(debug=True)
