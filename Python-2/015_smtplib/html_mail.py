import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = 'smtp.gmail.com'
PORT = '587'

FROM_MAIL = 'nitesh11041999@gmail.com'
TO_MAIL = 'nitesh20311@gmail.com'
PASSWORD = getpass.getpass("Enter password: ")

message = MIMEMultipart("alternative")
message['Subject'] = 'HTML test mail from python'
message['From'] = FROM_MAIL
message['To'] = TO_MAIL
message['Cc'] = FROM_MAIL
message['Bcc'] = FROM_MAIL


html = ""
with open('mail_html.html', 'r') as file:
    html = file.read()

html_part = MIMEText(html, 'html')
message.attach(html_part)


smtp = smtplib.SMTP(HOST, PORT)

status_code, responce = smtp.ehlo()
print(f"Ehloing the smtp server {status_code} {responce}")

status_code, responce = smtp.starttls()
print(f"Starting TLS for security {status_code} {responce}")

status_code, responce = smtp.login(FROM_MAIL, PASSWORD)
print(f"Logging into the smtp server {status_code} {responce}")

smtp.sendmail(FROM_MAIL, TO_MAIL ,message.as_string())
smtp.quit()

print("Mail Sent!!")