import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path(Path.cwd(), "email_playground", "index.html").read_text())

sender = {
    'email': 'anderson.john.python@gmail.com',
    'password': 'jjkqqhqbgsjyntys'
}
email = EmailMessage()
email['from'] = "Leo Anderson"
email['to'] = "thinh.nvq.js220597@gmail.com"
email["subject"] = "testing email sender in python using smtblib"

email.set_content(html.substitute({"name": "Thinh"}), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender['email'], sender['password'])
    smtp.send_message(email)
    print("All done!")
