# IMPORTAR EL MODULO SOCKET
from socket import *

def base(n):
	b = bin(n)[2:]
	o = oct(n)[2:]
	h = hex(n)[2:]
	return f"Bin: {b} Oct: {o} Hex:{h}"


# CREAR EL SOCKET DEL SERVIDOR
ADDR = ('localhost', 9876)
srvsock = socket(AF_INET, SOCK_DGRAM)
srvsock.bind(ADDR)

while True:
	print("Esperando mensajes...")
	# RECIBIMOS LA DATA Y LA IP DEL CLIENTE
	data, addr = srvsock.recvfrom(200)

	numero = int(data.decode("utf-8"))
	print(numero)
	# ALGORITMO PARA CONVERTIR LAS BASES NUMERICAS
	if 0 <= numero <= 255:
		resp = base(numero)
	else:
	 	resp = "Numero fuera de rango (0-255)"
	# ENVIAR DATA AL CLIENTE
	srvsock.sendto(resp.encode("UTF-8"), addr)
srvsock.close()





