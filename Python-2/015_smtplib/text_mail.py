import smtplib
import getpass
from art import text2art

HOST = 'smtp.gmail.com'
PORT = '587'

FROM_MAIL = 'nitesh11041999@gmail.com'
TO_MAIL = 'nitesh20311@gmail.com'
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE = """Subject: mail from pyhton script
We are testing mail.
This is message from python script
"""

smtp = smtplib.SMTP(HOST, PORT)

print(text2art("SMTP Python Script"))

status_code, response = smtp.ehlo()
print(f"Ehloing the server {status_code} {response}")

status_code, response = smtp.starttls()
print(f"Starting TLS connection {status_code} {response}")

status_code, response = smtp.login(FROM_MAIL, PASSWORD)
print(f"Logging into email {status_code} {response}")

smtp.sendmail(FROM_MAIL, TO_MAIL, MESSAGE)
smtp.quit()

print("Mail Sent!!")