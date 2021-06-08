import mysql
from flask import Flask,url_for, redirect
from flask import render_template
from flask import request
from flask import session


app = Flask(__name__,static_url_path='/static')

@app.route('/CV.html')
@app.route('/')
def index():
    return render_template('CV.html')

@app.route('/MYCV.html')
def mycv():
    return render_template('/MYCV.html')
@app.route('/ContactList.html')
def contact():
    return render_template('/ContactList.html')

@app.route('/contact_us.html')
def contactus():
    return render_template('contact_us.html')
@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html',
    user = {'firstname': "אופיר", 'lastname': "אביטבול"},
    hobbies=['לקרוא ספרים','לאפות עוגיות','להיפגש עם חברים'])

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    name = 'NONE'
    Users = {"Michael" :" Lawson", "Lindsay": " Ferguson", "Tobias" :" Funke", "Byron" :"Fields", "George": "Edwards","Rachel" : "Howell"}
    username = ' '
    logged_in = True

    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username


    return render_template('assignment9.html',
                           request_method=request.method,
                           name = name,
                           Users = Users,
                           username = username)

@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect('assignment9.html')

from Assignment10.Assignment10 import Assignment10
app.register_blueprint(Assignment10)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value



if __name__ == '__main__':
    app.run()
