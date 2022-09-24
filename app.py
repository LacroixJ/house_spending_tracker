#!/usr/bin/env python3
from flask import render_template, request, redirect, url_for, Flask
import os.path
import sqlite3

from datetime import datetime

app = Flask(__name__)

DB = 'db.db'

def get_users():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute('select distinct username from usernames;')
        data = [t[0] for t in cursor.fetchall()]
        return data

@app.route('/', methods=['GET'])
def homepage():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute('select *, ROWID from purchases order by -date(entrydate), -ROWID;')

        purchases = cursor.fetchall();

        totals = cursor.execute('select username, sum(price) from purchases group by username;')

        totals = cursor.fetchall()

        return render_template('home.html', purchases=purchases, totals=totals)


@app.route('/add_entry/', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        f = request.form
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute('insert into purchases values(?, ?, ?, ?)',
                    (f['name'], f['item_name'], float(f['price']), datetime.now().date()))
            conn.commit()
        return redirect(url_for('homepage'))
    return render_template('add_entry.html', names=get_users())

@app.route('/delete/', methods=['POST'])
def delete():
    f = request.form
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE from purchases where ROWID=?;', f['ROWID'])
        conn.commit()
    return redirect(url_for('homepage'))


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
