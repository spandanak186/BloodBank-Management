from flask import Blueprint, render_template, request, redirect
import sqlite3
from config import DB_PATH

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
        data = cur.fetchone()
        conn.close()

        if data:
            return redirect('/dashboard')
        else:
            return "Invalid login"

    return render_template("login.html")

@auth_bp.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (user, pwd))
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template("register.html")
