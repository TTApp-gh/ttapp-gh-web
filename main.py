#!/usr/bin/python3

'''
    This Controls The Server, Route And View Of Our App.
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    app_name = "TTApp"
    title = 'Welcome to TTApp!'
    return render_template('index.py', title=title, app_name=app_name)

@app.route('/about/')
def about():
    title = 'About Us'
    return render_template('about.html', title=title)
    
@app.route('/contact/')
def contact():
    title = "Contact Us"
    app_name = "Doziem"
    return render_template("contact.py", title=title, app_name=app_name)

if __name__ == '__main__':
    app.run(debug=True)