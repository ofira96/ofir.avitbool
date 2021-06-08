from flask import  Blueprint, render_template, request, url_for, redirect, flash
import mysql.connector

Assignment10 = Blueprint('Assignment10', __name__,
                          static_folder='static',
                          static_url_path='/Assignment10',
                          template_folder='templates')


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

@Assignment10.route('/Assignment10', methods=['GET', 'POST'])
def users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('Assignment10.html', users=query_result)

@Assignment10.route('/Add_user', methods=['GET', 'POST'])
def Add_user():
        if request.method == 'POST':
            username = request.form['username']
            Password = request.form['Password']
            query = "INSERT INTO users(username, Password) VALUES ('%s', '%s', '%s')" % (username, Password)
            interact_db(query=query, query_type='commit')
            flash('You were successfully insert a new user')
        return redirect('/Assignment10')

@Assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method =='GET':
        user_name =request.args['username']
        query = "DELETE FROM users Where username='%s';" % user_name
        interact_db(query=query, query_type='commit')
        flash('You were successfully delete user')
        return redirect('/Assignment10')

@Assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'GET':
        username = request.args['username']
        Password = request.args['Password']
        query = "UPDATE users SET username = %s WHERE Password= %s" % (username, Password)
        interact_db(query=query, query_type='commit')
        flash('You were successfully update  the user with the Password- %s' % Password)
        return redirect('/Assignment10')