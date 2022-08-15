"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template
from flask import url_for, request, redirect, session

import pymysql
import os

app = Flask(__name__)
app.secret_key = 'Thisismysecret'
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
unix_socket = '/cloudsql/{}'.format(db_connection_name)


database = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
cursor=database.cursor()

def getData():
    cursor=database.cursor()
    cursor.execute('Select * From experience')
    experience = cursor.fetchall()
    cursor.execute('Select * From projects')
    projects = cursor.fetchall()
    cursor.execute('Select * From education')
    education = cursor.fetchall()
    #print (experience)
    cursor.execute('Select * From bio where id = 0')
    bio = cursor.fetchone()
    cursor.execute('Select * From acheivements where id = 0')
    acheivements = cursor.fetchone()
    cursor.execute('Select * From skills where id = 0')
    skills = cursor.fetchone()

    return experience,projects,education,bio,acheivements,skills


@app.route('/')
def hello():
    """Renders a sample page."""
    experience,projects,education,bio,acheivements,skills = getData()
    return render_template('index.html',experience = experience,bio = bio , acheivements = acheivements,projects=projects,education = education,skills = skills)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        cursor=database.cursor()
        cursor.execute('SELECT id,username,level FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
       
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['level'] = account['level']
            return redirect(url_for('edit'))
        else:
            msg = 'Incorrect username/password!'
            return 'Error'
    return render_template('login.html')


@app.route('/edit',methods = ['GET'])
def edit():
    #print(session['loggedin'])
    if session.get('loggedin') == None or session.get('level') == None:
        return redirect(url_for('login'))
    experience,projects,education,bio,acheivements,skills = getData()
    return render_template('edit.html',experience = experience,bio = bio , acheivements = acheivements,projects=projects,education = education,skills = skills)

    
@app.route("/edit_bio",methods=['POST'])
def edit_bio():
    if session.get('loggedin') == None or session.get('level') == None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        field = request.form['id']
        value = request.form['val']
        cursor=database.cursor()
        if field == 'phone':
            cursor.execute("UPDATE bio SET phone = %s WHERE id = %s ", [value,0])
        elif field == 'linkedin':
            cursor.execute("UPDATE bio SET linkedin = %s WHERE id = %s ", [value,0])
        elif field == 'leetcode':
            cursor.execute("UPDATE bio SET leetcode = %s WHERE id = %s ", [value,0])
        elif field == 'github':
            cursor.execute("UPDATE bio SET github = %s WHERE id = %s ", [value,0])
        elif field == 'email':
            cursor.execute("UPDATE bio SET email = %s WHERE id = %s ", [value,0])
        else :
            cursor.execute("UPDATE bio SET about = %s WHERE id = %s ", [value,0])
        database.commit()
        return 'Success'

@app.route("/edit_education",methods=["POST"])
def edit_education(): 
    if session.get('loggedin') == None or session.get('level') == None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        institute = request.form['institute']
        course = request.form['course']
        gpa = request.form['gpa']
        iid = request.form['id']
        cursor=database.cursor()
        cursor.execute("UPDATE education SET course = %s,gpa = %s,institute = %s WHERE id = %s ", [course,gpa,institute,iid])
        database.commit()
        return 'Success'

@app.route("/edit_acheivements",methods=["POST"])
def edit_acheivements(): 
    if session.get('loggedin') == None or session.get('level') == None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        experience = request.form['experience']
        gate = request.form['gate']
        leetcode = request.form['leetcode']
        cursor=database.cursor()
        cursor.execute("UPDATE acheivements SET experience = %s,gate = %s,leetcode = %s WHERE id = %s ", [experience,gate,leetcode,0])
        database.commit()
        return 'Success'

@app.route("/edit_experience",methods=["POST"])
def edit_experience(): 
     if session.get('loggedin') == None or session.get('level') == None:
        return redirect(url_for('login'))

     if request.method == 'POST':
        description = request.form['description']
        eid = request.form['id']
        cursor=database.cursor()
        cursor.execute("UPDATE experience SET description = %s WHERE id = %s ", [description,eid])
        database.commit()
        return 'Success'

@app.route("/edit_project",methods=["POST"])
def edit_projects(): 
     if session.get('loggedin') == None or session.get('level') == None:
        return redirect(url_for('login'))

     if request.method == 'POST':
        about = request.form['about']
        title = request.form['title']
        pid = request.form['id']
        cursor=database.cursor()
        cursor.execute("UPDATE projects SET about = %s,title = %s WHERE  id = %s ", [about,title,pid])
        database.commit()
        return 'Success'

@app.route("/edit_skills",methods=["POST"])
def edit_skills(): 
    if session.get('loggedin') == None or session.get('level') == None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        cpp = request.form['cpp']
        java = request.form['java']
        html = request.form['html']
        python = request.form['python']
        mysql = request.form['mysql']
        php = request.form['php']
        cursor=database.cursor()
        cursor.execute("UPDATE skills SET cpp = %s,java = %s,python = %s,mysql = %s,php = %s,html = %s WHERE id = %s ", [cpp, java,python,mysql,php,html,0])
        database.commit()
        return 'Success'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
