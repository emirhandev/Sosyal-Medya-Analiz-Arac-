import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email():
    sender_email = "sender_mail"
    to_email = "to_email"
    sender_password = "sender_password"
    smtp_server = "smtp.gmail.com"
    attachment_path = "report.png"
    body = "Sosyal Medya Analiz Raporu Ektedir..."
    subject = "-Sosyal Medya Analiz Aracı-"
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_path}",
        )
        message.attach(part)
    try:
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit()
        print("E-posta gönderildi!")
    except Exception as e:
        print("E-posta gönderme hatası:", e)


