#!/usr/bin/env python3


from flask import render_template, request, redirect, url_for, Flask
import os.path
import yaml


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
        items = info[name].get('items')
        total = sum([list(item.values())[0] for item in items])
        info[name]['total'] = total



    return render_template('home.html', db=info)


@app.route('/add_entry/', methods=['GET', 'POST'])
def add_entry():
    info = load_db()
    names = info.keys()
    if request.method == 'POST':
        f = request.form
        info[f['name']]['items'].append({f['item']:float(f['price'])})
        db = open(DB, 'w')
        yaml.dump(info, db)
        db.close()
        return redirect(url_for('homepage'))
    return render_template('add_entry.html', names=names)



@app.route('/delete/', methods=['POST'])
def delete():
    info = load_db()
    f = request.form

    items = info[f['name']]['items']

    found = False
    for idx, item in enumerate(list(items)):
        for k, v in item.items():
            if k == f['item'] and v == float(f['price']):
                items.remove(item)
                found = True
        if found: break



    info[f['name']]['items'] = items

    db = open(DB, 'w')
    yaml.dump(info, db)
    db.close()

    return redirect(url_for('homepage'))


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
