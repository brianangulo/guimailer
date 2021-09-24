import smtplib, ssl

def sendEmail(recipient):
    port = 587
    password = "Fries@10"
    context = ssl.create_default_context()
    my_email = "brianportfolio219@gmail.com"
    msg = "fool"
    smtp_server = "smtp.gmail.com"

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(my_email, password)
        server.sendmail(my_email, recipient, msg)

pedyo = "pedrosanchez707@gmail.com"
brian = "brianangulo96@gmail.com"
i = 1
while i < 100:
    sendEmail(pedyo)
    print("Sent " + str(i))
    i = i + 1




