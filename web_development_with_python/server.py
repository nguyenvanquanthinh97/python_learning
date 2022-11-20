from flask import Flask, render_template, request, redirect
from sending_email import sending_email
from saving_db import saving_to_db

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=["GET", "POST"])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()

        email = data['email']
        subject = data['subject']
        message = data['message']

        saving_to_db(**data)
        # sending_email(email, subject, message)
        return redirect('/thankyou.html')

    else:
        return 'something went wrong. Try again'

