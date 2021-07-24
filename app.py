#!/usr/bin/env python3


from flask import render_template, request, redirect, url_for, Flask
import os.path
import yaml

from datetime import datetime


app = Flask(__name__)

DB = 'db.yaml'

def load_db():
    db = open(DB, 'r')
    info = yaml.safe_load(db)
    db.close()

    return info


@app.route('/', methods=['GET'])
def homepage():
    if not os.path.isfile(DB):
        file = open(DB, 'w')
        file.close()

    info = load_db()

    names = info.keys()


    for name in info.keys():
        purchases = info[name].get('purchases')

        total = 0
        for purchase in purchases:
            details = purchase['purchase']
            total += float(details['price'])

        info[name]['total'] = total



    return render_template('home.html', db=info)


@app.route('/add_entry/', methods=['GET', 'POST'])
def add_entry():
    info = load_db()
    names = info.keys()
    if request.method == 'POST':
        f = request.form
        purchase = {
                'purchase':
                    {
                    'name': f['item_name'],
                    'price': float(f['price']),
                    'date_added': datetime.now()
                    }
                }
        info[f['name']]['purchases'].append(purchase)
        db = open(DB, 'w')
        yaml.dump(info, db)
        db.close()
        return redirect(url_for('homepage'))
    return render_template('add_entry.html', names=names)



@app.route('/delete/', methods=['POST'])
def delete():
    info = load_db()
    f = request.form

    purchases = info[f['name']]['purchases']

    for purchase in purchases.copy():
        details = purchase['purchase']
        requirements = [
                details['name'] == f['item_name'],
                details['price'] == float(f['price']),
                ]
        if all(requirements):
            purchases.remove(purchase)
            break

    info[f['name']]['purchases'] = purchases

    db = open(DB, 'w')
    yaml.dump(info, db)
    db.close()

    return redirect(url_for('homepage'))


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
