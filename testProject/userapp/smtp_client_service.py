import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import random
from celery import shared_task
from .redis_service import add_cache


@shared_task
def send_verification_email(email):
    from_mail = os.getenv("SMTP_FROM_MAIL")
    from_passwd = os.getenv("SMTP_FROM_PASSWORD")
    server_adr = os.getenv("SMTP_SERVER_ADDR")
    to_mail = email

    msg = MIMEMultipart()
    msg["From"] = from_mail
    msg['To'] = to_mail
    msg["Subject"] = Header('Подтверждение регистрации', 'utf-8')
    msg["Date"] = formatdate(localtime=True)

    code = random.randint(1000, 9999)
    msg.attach(MIMEText("У вас 5 минут. Код подтверждения: " + str(code), 'html', 'utf-8'))
    add_cache(email, code, 300)

    smtp = smtplib.SMTP(server_adr, 25)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(from_mail, from_passwd)
    smtp.sendmail(from_mail, to_mail, msg.as_string())
    smtp.quit()
