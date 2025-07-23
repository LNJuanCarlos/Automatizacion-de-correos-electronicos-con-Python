import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración de tu correo y contraseña de aplicación
TU_CORREO = "ramnia02@gmail.com"
CONTRASENA = "bajs cefk iiuh xykj"

# Leer archivo Excel
df = pd.read_excel("correos.xlsx")  # Asegúrate que esté en la misma carpeta

# Conectarse al servidor SMTP de Gmail
servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()
servidor.login(TU_CORREO, CONTRASENA)

# Recorrer cada fila del Excel
for index, fila in df.iterrows():
    nombre = fila['nombre']
    correo = fila['email']

    # Crear mensaje personalizado
    asunto = "Hola desde Python, " + nombre
    mensaje_html = f"""
    <html>
        <body>
            <p>Hola {nombre},<br><br>
            Este es un correo automático enviado desde Python usando un Excel.<br>
            ¡Espero que tengas un excelente día!<br><br>
            Atentamente,<br>
            JuanCarlos
            </p>
        </body>
    </html>
    """

    # Construir el mensaje
    msg = MIMEMultipart()
    msg['From'] = TU_CORREO
    msg['To'] = correo
    msg['Subject'] = asunto
    msg.attach(MIMEText(mensaje_html, 'html'))

    try:
        servidor.sendmail(TU_CORREO, correo, msg.as_string())
        print(f"✅ Correo enviado a: {correo}")
    except Exception as e:
        print(f"❌ Error al enviar a {correo}: {e}")

# Cerrar conexión
servidor.quit()