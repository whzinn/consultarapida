import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import random
import string

def gerar_letras_aleatorias():
    letras = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return letras





# Configurações do servidor SMTP
smtp_server = 'smtp-relay.brevo.com'
smtp_port = 587  # Substitua pela porta SMTP apropriada

smtp_username = 'kulioshances@gmail.com'

smtp_password = '2Evs0xInaKYhbDdj'


# Configuração da mensagem de email
from_email = 'kulioshances@gmail.com'



# Adicione o corpo do email


def send(email, placa):
    letras_geradas = gerar_letras_aleatorias()
    subject = letras_geradas

    # Crie uma instância do objeto MIMEMultipart
    msg = MIMEMultipart()

    msg['From'] = from_email
    msg['Subject'] = subject

    to_email = email
    msg['To'] = email
    body = f'Pague sua consulta placa acesse <a href="https://pagamento.onrender.com/">Pagar</a>.'
    msg.attach(MIMEText(body, 'plain'))

    # Conecte-se ao servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use SSL/TLS para criptografar a conexão (pode variar conforme o servidor)

    # Faça login na conta
    server.login(smtp_username, smtp_password)

    # Envie o email
    server.sendmail(from_email, to_email, msg.as_string())

    # Encerre a conexão
    server.quit()
