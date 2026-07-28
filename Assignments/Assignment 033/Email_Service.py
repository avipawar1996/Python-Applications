import smtplib
import ssl
from email_validator import validate_email, EmailNotValidError

from email.message import EmailMessage

def validate_email(email):
    try:
        return True

    except EmailNotValidError as e:
        return False

    

def send_email(sender_email, password, rec_email, subject, body, attachments=None):

    try:
        connectivity_status = check_smtp_connectivity("smtp.gmail.com", 465)
        if (not connectivity_status):
            return False
        
        msg = EmailMessage()
    
        msg["From"] = sender_email
        msg["To"] = rec_email
        msg["Subject"] = subject
    
        msg.set_content(body)
    
        if attachments:
            for file_path in attachments:
                fobj = open(file_path, "rb")
                file_data = fobj.read()
                file_name = fobj.name
    
                msg.add_attachment(
                    file_data,
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_name
                )
    
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
        server.login(sender_email, password)
        server.send_message(msg)

        return True
    except Exception:
        return False
    

def check_smtp_connectivity(server_address, port):
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(server_address, port, context=context)
        server.noop()
        return True
    except Exception as e:
        print(f"Connectivity issue: {e}")
        return False