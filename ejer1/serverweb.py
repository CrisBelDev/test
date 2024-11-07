import socket

nombre = "Cristian Abel Mamani Mamani"
carnet = "12452572"

# CREACION DEL SERVER WEB
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#poner la ip actual
serverSock.bind(("localhost", 9876))
serverSock.listen(2)

print("SERVIDOR ESTA EN ESPERA")

# RECIBIR PETICIONES GET DE LOS CLIENTES
sockCli, direccion = serverSock.accept()
# DECODIFICAMOS LA INFORMACION DEL CLIENTE
req = sockCli.recv(1024).decode("UTF-8")
# GET, POST, DELETE, HEADERS?
print("Solicitud ha sido recibida: ", req)

# ENVIAR UNA RESPUESTA CON ESTADO
resp = f"HTTP/1.1 200 OK\n\nNombre:{nombre}, Carnet:{carnet}"
sockCli.send(resp.encode("UTF-8"))
sockCli.close()
