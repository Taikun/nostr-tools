import os
import ecdsa
import binascii
from cryptography.fernet import Fernet
from getpass import getpass
import hashlib
import base64

# Generar una clave privada aleatoria de 32 bytes
private_key = os.urandom(32)
private_key_hex = binascii.hexlify(private_key).decode("utf-8")

# Crear el objeto de la clave privada en la curva secp256k1
sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)

# Obtener la clave pública en formato de bytes y luego a hexadecimal
public_key = sk.verifying_key.to_string()
public_key_hex = binascii.hexlify(public_key).decode("utf-8")

# Solicitar contraseña para encriptar
password = getpass("Introduce una contraseña para encriptar tu identidad: ")
key = hashlib.sha256(password.encode()).digest()
fernet_key = base64.urlsafe_b64encode(key[:32])  # Asegura que la clave tiene el formato esperado por Fernet
fernet = Fernet(fernet_key)

# Preparar el contenido de las claves
identity_data = f"Clave privada (hex): {private_key_hex}\nClave pública (hex): {public_key_hex}\n"

# Encriptar el contenido
encrypted_data = fernet.encrypt(identity_data.encode())

# Guardar el contenido encriptado en un archivo binario
with open("nostr_identity.enc", "wb") as f:
    f.write(encrypted_data)

# Convertir el texto encriptado a Base64 para copiar en Bitwarden
encrypted_data_b64 = base64.urlsafe_b64encode(encrypted_data).decode()

# Mostrar el texto encriptado en Base64
print("Identidad encriptada guardada en nostr_identity.enc")
print("\nTexto encriptado en Base64 (puedes copiar esto en tu gestor de contraseñas):")
print(encrypted_data_b64)
