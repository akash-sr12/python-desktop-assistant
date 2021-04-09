# (c) 2020 - Akash Sarkar
# email_nix

import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(0)
    server.ehlo()
    server.starttls()
    server.esmtp_features['auth'] = 'LOGIN PLAIN'
    server.login('your_email@example.com', 'your_password')
    server.sendmail('your_email@example.com', to, content)
    server.close()

def findReceiver(name):
    contacts = {"Sagar": "sagar@example.com",
                "Akaash": "akash@example.com"}
    try:
        receiverGmail = contacts[name]
        return receiverGmail
    except:
        return 0
