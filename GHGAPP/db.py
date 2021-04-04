import mysql.connector

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
		    user=current_app.config['MYSQL_USER'],
		    passwd=current_app.config['MYSQL_PASSWORD'],
		    database=current_app.config['MYSQL_DB'],
		    auth_plugin=current_app.config['MYSQL_AUTH_PLUGIN']
        )

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    # Tells the Flask to call the close_db  function when cleaning up after returning the response
    app.teardown_appcontext(close_db)