import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Datos de autenticación (rellena con los tuyos)
EMAIL_REMITENTE = 'ramnia02@gmail.com'
PASSWORD = 'bajs cefk iiuh xykj'  # No uses tu contraseña normal, usa una contraseña de aplicación

# Leer Excel
df = pd.read_excel("correos prueba.xlsx")

# Conexión SMTP
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL_REMITENTE, PASSWORD)

# Envío de correos
for index, row in df.iterrows():
    mensaje = MIMEMultipart()
    mensaje['From'] = EMAIL_REMITENTE
    mensaje['To'] = row['Email']
    mensaje['Subject'] = row['Asunto']

    cuerpo = row['Mensaje']
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    texto = mensaje.as_string()
    server.sendmail(EMAIL_REMITENTE, row['Email'], texto)
    print(f"Correo enviado a: {row['Email']}")

server.quit()