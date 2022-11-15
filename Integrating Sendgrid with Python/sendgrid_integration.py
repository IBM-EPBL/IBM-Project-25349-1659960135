from flask import Flask
from flask_mail import Mail, Message

# SENDER's and RECEIVER's mail have been hidden for privacy reasons

app = Flask(__name__)
mail = Mail(app) 

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'SENDER_MAIL'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    msg = Message(
				'Hello',
				sender ='SENDER_MAIL',
				recipients = ['RECEIVER_MAIL']
			   )
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return 'Sent'


if __name__ == '__main__':
    app.debug = True
    app.run()
