from socket import *
# CREACION DEL CLIENTE
ADDR = ("localhost", 9876)
cliSock = socket(AF_INET, SOCK_DGRAM)

# ENTRADA DE DATOS DESDE EL CLIENTE
data = input("Introduzca un numero: ")
# ENVIO DE DATOS HACIA EL SERVIDOR
cliSock.sendto(data.encode("UTF-8"), ADDR)
# RECEPCION DE DATOS DESDE EL SERVIDOR
data, ADDR = cliSock.recvfrom(200)
# MOSTRAMOS LA RESPUESTA DE LAS BASES NUMERICAS
print(data.decode("UTF-8"))

cliSock.close()

