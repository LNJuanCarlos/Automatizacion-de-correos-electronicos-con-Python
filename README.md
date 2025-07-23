Si se desea leer correo desde un excel, se tiene que usar Pandas
pip install pandas

Creamos un excel ejemplo: correo.xlsx con una hoja llamada Hoja1 y una columna llamada email

df = pd.read_excel("correos.xlsx")
destinatarios = df["email"].tolist()

Luego reemplaza la lista fija de correos con destinatarios = df["email"].tolist().


Instalar la librería openpyxl para poder leer archivos .xlsx
