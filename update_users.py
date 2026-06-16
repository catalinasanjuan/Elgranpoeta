import hashlib
import os
import mysql.connector
from config import db_config

# Conectar a la base de datos
db = mysql.connector.connect(**db_config)
cursor = db.cursor(dictionary=True)

# Función para crear hashed_password y salt
def create_hashed_password(password):
    salt = os.urandom(16).hex()
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return salt, hashed_password

# Obtener los usuarios existentes
cursor.execute("SELECT ID_Usuario, Nombre_Usuario FROM usuario")
usuarios = cursor.fetchall()

# Actualizar cada usuario con hashed_password y salt
for usuario in usuarios:
    username = usuario['Nombre_Usuario']
    # Aquí asumimos una contraseña predeterminada para cada usuario, puedes ajustar esto según tus necesidades.
    password = 'password123'
    salt, hashed_password = create_hashed_password(password)
    
    # Actualizar la tabla usuario
    cursor.execute("""
        UPDATE usuario 
        SET hashed_password = %s, salt = %s 
        WHERE ID_Usuario = %s
    """, (hashed_password, salt, usuario['ID_Usuario']))

# Confirmar los cambios en la base de datos
db.commit()

# Cerrar la conexión a la base de datos
cursor.close()
db.close()
