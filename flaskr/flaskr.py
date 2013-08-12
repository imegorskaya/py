from __future__ import with_statement
from contextlib import closing
from flask import Flask
import sqlite3

#configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
#===========================
#application

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


app = Flask(__name__)
app.config.from_object(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello World!'
#
if __name__ == '__main__':
    app.run()
