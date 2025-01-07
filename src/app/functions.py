import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .configuration import MAIL_FROM, MAIL_PASSWORD, LOGGER
from .models import EmailRequest


def send_message(email_request: EmailRequest):
    try:
        # Crear el mensaje
        message = MIMEMultipart()
        message["From"] = MAIL_FROM
        message["To"] = MAIL_FROM
        message["Subject"] = email_request.subject

        body = (f'Message from: {email_request.email}\n\n '
                f'{email_request.message}')
        # Agregar el cuerpo del mensaje
        message.attach(MIMEText(body, "plain"))

        # Conectar al servidor SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Iniciar conexión segura
            server.login(MAIL_FROM, MAIL_PASSWORD)  # Iniciar sesión
            server.send_message(message)  # Enviar el mensaje

        LOGGER.info("Email send")

    except Exception as e:
        LOGGER.error(f"Error to send the mail: {e}")
        raise e
