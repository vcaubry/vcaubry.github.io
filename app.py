import os
from flask import Flask, redirect, render_template, url_for, request, flash
from flask_script import Manager, Shell
from flask_mail import Message, Mail
from flask_wtf import FlaskForm
from flask_frozen import Freezer
from wtforms import Form, TextField, TextAreaField, SubmitField
from wtforms.validators import Required, Email
from contact import username

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
app.secret_key = 'Toasted bread is the best thing since sliced bread'

app.config.from_pyfile('settings.py')

manager = Manager(app)

@app.route('/')
@app.route('/index.html')
def about():
    return render_template("index.html")

@app.route('/services')
@app.route('/services.html')
def services():
    return render_template("services.html")

@app.route('/testimonials')
@app.route('/testimonials.html')
def testimonials():
    return render_template("testimonials.html")

@app.route('/contact', methods=["GET","POST"])
@app.route('/contact.html')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    manager.run(host='0.0.0.0', port=port)
