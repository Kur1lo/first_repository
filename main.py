from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/phones/create/')
def phones_create():
    phones = request.args['phones']
    contact_name = request.args['contact_name']

    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO phones
        VALUES ('{contact_name}', '{phones}');
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Done!'


@app.route('/phones/read/')
def email_read():
    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM phones;
        '''
        cur.execute(sql)
        phones = cur.fetchall()

    finally:
        conn.close()

    return str(phones)


@app.route('/phones/delete/')
def email_delete():
    phones = request.args['phones']

    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM phones WHERE phones == '{phones}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Delete Complete'


@app.route('/phones/update/')
def email_update():
    phones = request.args['phones']
    contact_name = request.args['contact_name']

    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE phones
        SET ContactName = '{contact_name}'
        WHERE phones == '{phones}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Update Complete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
