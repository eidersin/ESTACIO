# Import dos pacote necessários
import smtplib
import email.message


def enviar_email():
    # O código seguinte mostra a criação da mensagem com o corpo e seus parâmetros:
    # Criação de um objeto de mensagem
    corpo_email = "Mensagem de email"
    # Parâmetros
    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = "E-MAIL"
    msg['To'] = "Destinatario do email"
    password = "Senha do email"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    # Criação do servidor
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    # Login na conta para envio
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    # Encerramento do servidor
    # s.quit()
    print('Mensagem enviada com sucesso')


enviar_email()
