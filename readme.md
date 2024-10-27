Intrucciones:
1. Create un entorno virtual, por ejemplo en windows
    ```bash
    python -m venv .venvwin
    ```
2. Asegurate de activarlo, por ejemplo en windows powershell
   ```bash
   .\.venvwin\Scripts\Activate.ps1
   ```
3. Instala las despendencias
   ```bash
   pip install -r .\requirements.txt
   ```
4. Crea identidad encriptada
   ```bash
   python generate_identity.py
   ```
   Va a generar un fichero con la identidad encripta: nostr_identity.enc
   Una cadena de texto por la salida estandar para guardan en Bitwarden o cualquier gestor de contraseñas.
5. Desencripta identidad para llevarla a las aplicaciones
   ```bash
   python decrypt_identity.py
   ```

Cada uno se tiene qeu responsabilidad de custodiar a buen recaudo su identidad pero yo voy a guardarla encriptada en Bitwarden y la clave la dejaré en mi cabeza. Cuando una aplicación me la pida la desencripto, la copio y la destruyo.