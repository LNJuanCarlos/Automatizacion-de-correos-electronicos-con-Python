import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURACIÓN ---
remitente = 'ramnia02@gmail.com'            # <- Tu correo
destinatario = 'ramnia02@ejemplo.com'        # <- Destinatario
asunto = 'Correo automático desde Python'
mensaje = 'Hola, esto es una prueba de automatización.'

# CONTRASEÑA (usa contraseña de aplicación si Gmail con 2FA)
password = 'bajs cefk iiuh xykj'

# --- CREAR EL MENSAJE ---
msg = MIMEMultipart()
msg['From'] = remitente
msg['To'] = destinatario
msg['Subject'] = asunto
msg.attach(MIMEText(mensaje, 'plain'))

# --- ENVIAR ---
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remitente, password)
    servidor.sendmail(remitente, destinatario, msg.as_string())
    servidor.quit()
    print("✅ Correo enviado exitosamente.")
except Exception as e:
    print("❌ Error:", e)