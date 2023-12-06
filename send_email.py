import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "<Email-address>" # From address
    password = "<APP-password>" #Search in google how to get app password for smtp mail

    receiver = "<Receiver-email-address>" # Receive address

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)