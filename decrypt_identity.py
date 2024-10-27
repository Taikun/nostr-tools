import os
from cryptography.fernet import Fernet
from getpass import getpass
import hashlib
import base64

def load_identity_from_file():
    """Función para cargar y desencriptar la identidad desde un archivo encriptado."""
    if not os.path.exists("nostr_identity.enc"):
        print("El archivo 'nostr_identity.enc' no existe.")
        return

    with open("nostr_identity.enc", "rb") as f:
        encrypted_data = f.read()
    
    # Mostrar el contenido encriptado en Base64 para copiar en un gestor de contraseñas
    encrypted_data_b64 = base64.urlsafe_b64encode(encrypted_data).decode()
    print("\nContenido en Base64 para uso en Bitwarden u otro gestor:\n", encrypted_data_b64)

    # Pedir la contraseña para desencriptar
    password = getpass("\nIntroduce la contraseña para desencriptar tu identidad: ")
    decrypted_data = decrypt_identity(encrypted_data, password)
    
    if decrypted_data:
        print("Datos de la identidad cargados desde el archivo:\n", decrypted_data)

def input_encrypted_text_manually():
    """Función para introducir el texto encriptado manualmente y desencriptarlo."""
    encrypted_text = input("Introduce el texto encriptado (Base64) copiado de tu gestor de contraseñas: ").strip()
    
    try:
        encrypted_data = base64.urlsafe_b64decode(encrypted_text)
    except Exception:
        print("El texto encriptado no está en formato Base64 válido.")
        return

    password = getpass("Introduce la contraseña para desencriptar el texto: ")
    decrypted_data = decrypt_identity(encrypted_data, password)
    
    if decrypted_data:
        print("Datos de la identidad introducidos manualmente:\n", decrypted_data)

def decrypt_identity(encrypted_data, password):
    """Desencripta los datos encriptados usando una contraseña proporcionada."""
    # Generar una clave Fernet en formato Base64 seguro a partir de la contraseña
    key = hashlib.sha256(password.encode()).digest()[:32]
    fernet_key = base64.urlsafe_b64encode(key)
    fernet = Fernet(fernet_key)

    # Intentar desencriptar el contenido
    try:
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data
    except Exception:
        print("Error al desencriptar: contraseña incorrecta o datos encriptados inválidos.")
        return None

def main():
    choice = input("¿Quieres cargar la identidad desde el archivo (s) o introducir el texto encriptado manualmente (m)? ").strip().lower()

    if choice == 's':
        load_identity_from_file()
    elif choice == 'm':
        input_encrypted_text_manually()
    else:
        print("Opción no válida. Selecciona 's' para cargar desde el archivo o 'm' para introducir manualmente el texto encriptado.")

# Ejecutar la función principal
main()
