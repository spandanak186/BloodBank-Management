from flask import Blueprint, render_template, request
import sqlite3
from config import DB_PATH

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        blood = request.form['blood']

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT * FROM donors WHERE blood_group=?", (blood,))
        results = cur.fetchall()
        conn.close()

    return render_template("search.html", results=results)
