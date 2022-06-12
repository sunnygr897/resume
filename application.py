
from datetime import datetime
from logging import NullHandler
from flask import render_template 
import pandas as pd
from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)


import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal

config = {
  'host':'<127.0.0.1',
  'user':'root',
  'password':'toor',
  'database':'resume'
}

# Construct connection string


conn = mysql.connector.connect(**config)

cursor = conn.cursor(dictionary=True)

#app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'toor'
#app.config['MYSQL_DB'] = 'resume'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    #cursor = mysql.connection.cursor()
    cursor.execute("""SELECT * FROM skills where id = 0 """)
    skills = cursor.fetchone()
    cursor.execute("""SELECT * FROM bio where id = 0 """)
    bio = cursor.fetchone()
    return render_template('index.html',skills = skills,bio = bio)

if __name__ == '__main__':
    app.run()