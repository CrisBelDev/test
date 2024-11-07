# Importar módulo socket
from socket import *

# Función para convertir un número a bases numéricas
def base(n):
    b = bin(n)[2:]  # Conversión a binario
    o = oct(n)[2:]  # Conversión a octal
    h = hex(n)[2:].upper()  # Conversión a hexadecimal
    return f"bin: 0000{b} oct: {o} hex: {h}"

# Crear el socket del servidor
addr = ("localhost", 9876)
srvSock = socket(AF_INET, SOCK_DGRAM)
srvSock.bind(addr)

# Bucle de espera de mensajes
while True:
    print("Esperando mensajes...")
    data, client_addr = srvSock.recvfrom(200)
    numero = int(data.decode("utf-8"))
    print(numero)
    # Algoritmo para verificar y convertir las bases numéricas
    if 0 <= numero <= 255:
        resp = base(numero)
    else:
        resp = "Numero fuera de rango"

    # Enviar respuesta al cliente
    srvSock.sendto(resp.encode("utf-8"), client_addr)

# Cerrar el socket (esto nunca se ejecuta ya que el bucle es infinito)
srvSock.close()
