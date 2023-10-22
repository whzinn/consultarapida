import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configurações do servidor SMTP
smtp_server = 'smtp-relay.brevo.com'
smtp_port = 587  # Substitua pela porta SMTP apropriada

smtp_username = 'xmalesant@gmail.com'

smtp_password = 'qnvhWOfLJYm8zydg'   


# Configuração da mensagem de email
from_email = 'xmalesant@gmail.com'

to_email = 'bwmbybr@gmail.com'
subject = 'Alguém solicitou uma consulta placa'

# Crie uma instância do objeto MIMEMultipart
msg = MIMEMultipart()

msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# Adicione o corpo do email


def send(email, placa):
    body = f'''<!DOCTYPE html>
<html>
<head>
    <title>Pagamento de Consulta</title>
</head>
<body style="background-color: #3498db; text-align: center; color: white; font-size: 24px;">
    <div style="margin: 100px auto; max-width: 600px; padding: 20px;">
        <h1>Pague sua consulta via PIX para receber via e-mail</h1>
     
        <p>Assim que o pagamento for confirmado, você receberá os detalhes da sua consulta via e-mail.</p>
        <a href="https://pagamento.onrender.com/" style="text-decoration: none;">
            <button style="background-color: #e74c3c; color: white; border: none; border-radius: 50%; width: 100px; height: 100px; font-size: 24px; margin-top: 20px;">
                Pagar
            </button>
        </a>
    </div>
</body>
</html>
'''
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
