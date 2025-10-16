import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Carrega .env
#SMTP_SSL_HOST=mail.seudominio.com.br
#SMTP_SSL_PORT=465
#SMTP_USERNAME=bot@seudominio.com.br
#SMTP_PASSWORD=suasenha
#SMTP_FROM_ADDR=bot@seudominio.com.br
load_dotenv()

def send_mail(the_message, subject, to_addr): 
    smtp_ssl_host = os.environ['SMTP_SSL_HOST']
    smtp_ssl_port = int(os.environ['SMTP_SSL_PORT'])
    username = os.environ['SMTP_USERNAME']
    password = os.environ['SMTP_PASSWORD']
    from_addr = os.environ['SMTP_FROM_ADDR']

    message = MIMEMultipart()
    message['subject'] = subject
    message['from'] = from_addr
    message['to'] = ', '.join(to_addr)
    message.attach(MIMEText(the_message, "html"))

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(from_addr, to_addr, message.as_string())
    server.quit()