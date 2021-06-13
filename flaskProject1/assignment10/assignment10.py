import mysql
from flask import render_template, Blueprint, request, flash, redirect

# assignment10 blueprint
from app import interact_db


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


assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')


# routes
@assignment10.route('/assignment10')
def users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/Add_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        username = request.form['username']
        Email = request.form['Email']
        Password = request.form['Password']
        query = "INSERT INTO users(username,Email, Password) VALUES ('%s', '%s', '%s')" % (username, Email, Password)
        interact_db(query=query, query_type='commit')
        #  flash('You were successfully insert new user')
        return redirect('/assignment10')
        return render_template('assignment10.html', requemeth=request.method)


@assignment10.route('/delete_user', methods=['POST'])
def delete_user():
        user_name = request.form['username']
        query = "DELETE FROM users Where username='%s';" % user_name
        interact_db(query=query, query_type='commit')
        # flash('You were successfully delete user')
        return redirect('/assignment10')
        return render_template('assignment10.html', requemeth=request.method)

@assignment10.route('/update_user', methods=['POST'])
def update_user():
        username = request.form['username']
        Email = request.form['Email']
        Password = request.form['Password']
        query = "UPDATE users SET username= '%s', Password = '%s' WHERE Email= '%s'" % (username, Password ,Email)
        interact_db(query=query, query_type='commit')
        #flash('You were successfully update  the user with the Password- %s' % Password)
        return redirect('/assignment10')
        return render_template('assignment10.html', requemeth=request.method)
