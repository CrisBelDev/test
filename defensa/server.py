import socket
import threading

# Crear matriz de 5 filas x 10 columnas para el teatro
seats = [["-" for _ in range(10)] for _ in range(5)]
capacity = 50  # aforo total
reserved_seats = 0

# Función para mostrar el estado de las sillas
def display_seats():
    print("Estado actual de las sillas (Ocupadas = X, Libres = -):")
    for row in seats:
        print(" ".join(row))
    print("\n")

# Manejar la reserva del cliente
def handle_client(client_socket):
    global reserved_seats

    try:
        # Recibir el apellido y la cantidad de personas
        data = client_socket.recv(1024).decode()
        apellido, quantity = data.split(",")
        quantity = int(quantity)
        
        if quantity <= 0:
            client_socket.send("Error: La cantidad debe ser mayor que cero.\n".encode())
            client_socket.close()
            return
        
        # Verificar si hay suficientes asientos libres
        if reserved_seats + quantity > capacity:
            client_socket.send("Error: No hay suficientes asientos disponibles.\n".encode())
            client_socket.close()
            return
        
        # Realizar la reserva
        seats_reserved = 0
        for i in range(5):
            for j in range(10):
                if seats[i][j] == "-":
                    seats[i][j] = "X"
                    seats_reserved += 1
                    reserved_seats += 1
                    if seats_reserved == quantity:
                        display_seats()
                        client_socket.send(f"Reserva exitosa para {apellido}. Sillas reservadas: {quantity}\n".encode())
                        client_socket.close()
                        return
        
        client_socket.send("Error: No se pudieron reservar suficientes sillas.\n".encode())
    finally:
        client_socket.close()

# Configuración del servidor
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(5)
    print("Servidor iniciado en el puerto 9999...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexión aceptada desde {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
