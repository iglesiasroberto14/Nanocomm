## Organizador de cuentas por Minorista
### Requerimientos
 + Tener instalado Python 3 en la PC
  - https://www.python.org/downloads/
 + Archivos `cuenta.json` y `minorista.json` del cliente

### Como usar
 + Descargar el script `organizador_v1.py`
 + Colocar en la misma carpeta que los archivos `cuenta.json` y `minorista.json`
 + Ejecutar el script con doble clic

### Que esperar
 + El script devolvera 3 archivos:
  - `cuentaNuevo.json`: el archivo que va a remplazar `cuenta.json` en el cliente
  - `cuentas_ok.txt`: formato `ID_MINORISTA`,`ID_COMUNICADOR`
  - `cuentas_sin_minorista.txt`: `ID_MINORISTA`,`ID_COMUNICADOR
 + El script devolvera en pantalla los contadores de cuentas ok y cuentas sin minorista.
