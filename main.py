"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template 
#import mysql.connector
import pymysql
import os

app = Flask(__name__)

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
unix_socket = '/cloudsql/{}'.format(db_connection_name)


conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
cursor=conn.cursor()



@app.route('/')
def hello():
    """Renders a sample page."""
    #skills = cursor.execute('Select * From skills where id = 0')
    cursor.execute('Select * From experience where id = 0')
    experience = cursor.fetchall()
    cursor.execute('Select * From projects where id = 0')
    projects = cursor.fetchall()
    cursor.execute('Select * From education where id = 0')
    education = cursor.fetchall()
    print (experience)
    cursor.execute('Select * From bio where id = 0')
    bio = cursor.fetchone()
    cursor.execute('Select * From acheivements where id = 0')
    acheivements = cursor.fetchone()
    cursor.execute('Select * From skills where id = 0')
    skills = cursor.fetchone()
    return render_template('index.html',experience = experience,bio = bio , acheivements = acheivements,projects=projects,education = education,skills = skills)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
