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

mail = Mail()

app = Flask(__name__)
app.debug = True
app.secret_key = 'Toasted bread is the best thing since sliced bread'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = username
# app.config["MAIL_PASSWORD"] = password

mail.init_app(app)

manager = Manager(app)

class ContactForm(FlaskForm):
    email = TextField("Email", validators=[Required(), Email()], description="Email", render_kw={"placeholder": "Email"})
    name = TextField("Name", validators=[Required()], description="Name", render_kw={"placeholder": "Name"})
    subject = TextField("Subject", validators=[Required()], description="Subject", render_kw={"placeholder": "Subject"})
    message = TextAreaField("Message", validators=[Required()], description="Message", render_kw={"placeholder": "Message"})
    submit = SubmitField('Submit')

@app.route('/')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")

@app.route('/contact', methods=["GET","POST"])
def contact():
    # form = ContactForm()
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         msg = Message(form.subject.data, sender=username, recipients=["vcaubry@gmail.com"])
    #         msg.body = """
    #         From %s <%s>
    #         %s
    #         """ % (form.name.data, form.email.data, form.message.data)
    #         mail.send(msg)
    #         flash("Message sent!")
    #     flash("Please fill out all fields to submit.")
    #     return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == '__main__':
    manager.run()
