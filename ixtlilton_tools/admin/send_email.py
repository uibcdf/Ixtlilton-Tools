import smtplib
import ssl
import os

def send_mail(username, mimemultipart):

    usermail = get_email_from_user(username)

    context = ssl.create_default_context()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login('uibcdf@gmail.com', os.environ['UIBCDF_MAIL'])
    server.sendmail('uibcdf@gmail.com', usermail, mimemultipart.as_string())
    server.quit()

    pass

