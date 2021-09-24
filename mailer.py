import smtplib, ssl

def send_email(recipient, pwd, sender_email, message):
    port = 587
    password = pwd
    context = ssl.create_default_context()
    my_email = sender_email
    msg = message
    smtp_server = "smtp.gmail.com"

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(my_email, password)
        server.sendmail(my_email, recipient, msg)
        server.quit()


def mail_loop(recipient, pwd, sender_email, message, max):
    i = 0
    while i < max:
        send_email(recipient, pwd, sender_email, message)
        print("Sent " + str(i))
        i = i + 1


