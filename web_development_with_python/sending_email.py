import smtplib
from email.message import EmailMessage


def sending_email(sender_email, subject, message):
    account = {
        'email': 'anderson.john.python@gmail.com',
        'password': 'jjkqqhqbgsjyntys'
    }
    email = EmailMessage()
    email['to'] = "thinh.nvq.js220597@gmail.com"
    email["subject"] = f"From: {sender_email}__{subject}"
    email.set_content(f"From: {sender_email}\n{message}")

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(account['email'], account['password'])
        smtp.send_message(email)
        print("All done!")
