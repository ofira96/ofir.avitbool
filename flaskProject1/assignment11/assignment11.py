import mysql
from flask import render_template, Blueprint, request, flash, redirect,jsonify

# assignment11 blueprint
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


assignment11 = Blueprint('assignment11', __name__,
                         static_folder='static',
                         static_url_path='/assignment11',
                         template_folder='templates')

# routes
@assignment11.route('/assignment11/users',methods=['GET'])
def users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    query_result = jsonify(query_result)
    return query_result
@assignment11.route('/assignment11/users/selected', defaults={'specific_user': 0})
@assignment11.route('/assignment11/users/selected/<int:specific_user>',methods=['GET'])
def find_user(specific_user):
    userExiste= specific_user in [1,2,3,4,5,6]
    userId = {}
    query = ("select * from users where userId =" + str(specific_user))
    query_result = interact_db(query, query_type='fetch')
    if (userExiste):
        query_result = jsonify(query_result)

    else:
        if len(query_result) == 0:
            query_result = jsonify('there is no such a user please try again')

        else:
            query = "select * from users where userId = 0 "
            query_result = interact_db(query, query_type='fetch')
            query_result = jsonify(query_result)
    return query_result

