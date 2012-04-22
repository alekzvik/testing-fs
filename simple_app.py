from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sendmail import Mail, Message

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

mail = Mail(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send_mail', methods=['POST'])
def send_mail():
    msg = Message(
        subject=request.form['subject'],
        recipients=list(request.form['recipients']),
        sender=request.form['sender'],
        body=request.form['body'],
    )
    mail.send(msg)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
