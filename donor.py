from flask import Blueprint, render_template, request, redirect
import sqlite3
from config import DB_PATH

donor_bp = Blueprint('donor', __name__)

@donor_bp.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@donor_bp.route('/add_donor', methods=['GET', 'POST'])
def add_donor():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood = request.form['blood']
        phone = request.form['phone']
        city = request.form['city']

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("INSERT INTO donors (name, age, blood_group, phone, city) VALUES (?,?,?,?,?)",
                    (name, age, blood, phone, city))
        conn.commit()
        conn.close()

        return redirect('/dashboard')

    return render_template("donor_register.html")
