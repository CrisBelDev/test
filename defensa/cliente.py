import socket

# Función para realizar la reserva
def make_reservation(apellido, quantity):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))
    
    # Enviar apellido y cantidad de personas
    data = f"{apellido},{quantity}"
    client_socket.send(data.encode())
    
    # Recibir respuesta del servidor
    response = client_socket.recv(1024).decode()
    print(response)
    
    client_socket.close()

# Ejemplo de uso
if __name__ == "__main__":
    apellido = input("Ingrese su apellido: ")
    quantity = int(input("Ingrese la cantidad de personas: "))
    make_reservation(apellido, quantity)
