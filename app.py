import os
from flask import Flask, redirect, render_template, url_for, request, flash
from flask_script import Manager, Shell
from flask_mail import Message, Mail
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, SubmitField
from wtforms.validators import Required, Email
from contact import username

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
app.secret_key = 'Toasted bread is the best thing since sliced bread'

manager = Manager(app)

@app.route('/')
def about():
    return render_template("index.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")

@app.route('/contact', methods=["GET","POST"])
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    manager.run()
