
from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from decouple import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_feedback_email_task(name, email, review):
	context = {
		'name': name,
		'email': email,
		'review': review,

	}
	email_subject ='Review'
	email_body = render_to_string('email_message.txt', context)
	sender_email = config('MY_EMAIL')
	receiver_email = config('EMAIL_TO')

	message = MIMEMultipart()
	message['From'] = sender_email
	message['To'] = receiver_email
	message['Subject'] = email_subject

	# Add message body
	body = "Hello, this is a test email."
	message.attach(MIMEText(email_body, 'plain'))

	# Create the SMTP server and send the email
	server = smtplib.SMTP('smtp.gmail.com', 587)

	server.starttls()  # Secure the connection
	print("Connection secured")
	server.login(sender_email, config('EMAIL_PASSWORD'))
	print("Logged in")
	text = message.as_string()
	server.sendmail(sender_email, receiver_email, text)
	server.quit()


