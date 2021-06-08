from flask import Flask,url_for
from flask import render_template


app = Flask(__name__,static_url_path='/static')

@app.route('/CV.html')
@app.route('/')
def index():
    return render_template('CV.html')

@app.route('/MYCV.html')
def mycv():
    return render_template('MYCV.html')
@app.route('/ContactList.html')
def contact():
    return render_template('/ContactList.html')

@app.route('/contact_us.html')
def contactus():
    return render_template('/contact_us.html')
@app.route('/assignment8.html')
def assignment8():
    return render_template('/assignment8.html',
    user = {'firstname': "אופיר", 'lastname': "אביטבול"},
    hobbies=['לקרוא ספרים','לאפות עוגיות','להיפגש עם חברים'])


if __name__ == '__main__':
    app.run()
