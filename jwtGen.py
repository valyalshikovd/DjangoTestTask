import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_server = "smtp.gmail.com "
smtp_port = 587
smtp_user = "your_email@example.com"
smtp_password = "your_password"

to_email = "recipient@example.com"

msg = MIMEMultipart()
msg["From"] = smtp_user
msg["To"] = to_email
msg["Subject"] = "Тестовое письмо с HTML и вложением"

html = """\
<html>
  <body>
    <h1 style="color: blue;">Привет!</h1>
    <p>Это <b>HTML</b> письмо с вложением.</p>
  </body>
</html>
"""
msg.attach(MIMEText(html, "html"))

# Добавляем вложение
filename = "document.pdf"  # Имя файла
filepath = "/path/to/document.pdf"  # Путь к файлу

with open(filepath, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(part)

# Отправка письма
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_user, smtp_password)
server.sendmail(smtp_user, to_email, msg.as_string())
server.quit()

print("Письмо отправлено с вложением!")
