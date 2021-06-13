from flask import Flask, redirect, render_template, request, session
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
#app.config.from_pyfile('settings.py')


@app.route('/CV')
@app.route('/')
def index():
    return render_template('CV.html')


@app.route('/MYCV')
def mycv():
    return render_template('MYCV.html')


@app.route('/ContactList')
def contact():
    return render_template('ContactList.html')


@app.route('/contact_us')
def contactus():
    return render_template('contact_us.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html',
                           user={'firstname': "אופיר", 'lastname': "אביטבול"},
                           hobbies=['לקרוא ספרים', 'לאפות עוגיות', 'להיפגש עם חברים'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    FirstName = 'NONE'
    Users = {"Michael": " Lawson", "Lindsay": " Ferguson", "Tobias": " Funke", "Byron": "Fields", "George": "Edwards",
             "Rachel": "Howell"}
    username = ' '
    logged_in = True
    if request.method == 'GET':
        if 'FirstName' in request.args:
            FirstName = request.args['FirstName']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username
    return render_template('assignment9.html',
                           request_method=request.method,
                           FirstName=FirstName,
                           Users=Users,
                           username=username)


@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect('assignment9')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='schema_users')
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


from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

from assignment11.assignment11 import assignment11
app.register_blueprint(assignment11)

if __name__ == '__main__':
    app.run(debug=True)
