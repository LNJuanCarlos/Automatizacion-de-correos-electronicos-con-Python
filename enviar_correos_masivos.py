import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd  # Solo si usas archivo con correos

# Configura tu correo y contraseña de aplicación (no tu contraseña real)
TU_CORREO = "ramnia02@gmail.com"
CONTRASENA = "bajs cefk iiuh xykj"

# Crea la conexión con el servidor SMTP
servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()
servidor.login(TU_CORREO, CONTRASENA)

# Lista de destinatarios (puedes cargar desde Excel o CSV con pandas si deseas)
destinatarios = [
    "ramnia02@gmail.com",
    "correo2@ejemplo.com",
    "correo3@ejemplo.com"
]

# Asunto y mensaje
asunto = "¡Hola desde Python!"
mensaje_html = """
<html>
  <body>
    <p>Hola,<br>
       Este es un correo automático enviado desde Python.<br>
       ¡Saludos!
       JuanCarlos
    </p>
  </body>
</html>
"""

# Enviar el correo a cada destinatario
for correo in destinatarios:
    msg = MIMEMultipart()
    msg['From'] = TU_CORREO
    msg['To'] = correo
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje_html, 'html'))

    try:
        servidor.sendmail(TU_CORREO, correo, msg.as_string())
        print(f"Correo enviado a: {correo}")
    except Exception as e:
        print(f"Error al enviar a {correo}: {e}")

# Cierra la conexión
servidor.quit()