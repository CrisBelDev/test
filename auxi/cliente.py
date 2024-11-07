from socket import *
# creacion del cliente
addr = ('localhost', 9876)

cliSock = socket(AF_INET, SOCK_DGRAM)
#entrada de datos desdel el cliente
data = input("introduzca un numero: ")

#envio de datos hacia el servidor
cliSock.sendto(data.encode("utf-8"),addr)
data, addr = cliSock.recvfrom(200)
#mostramos la respuesta de bases numericas
print(data.decode("utf-8"))
cliSock.close()
