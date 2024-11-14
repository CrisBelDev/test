import socket
import threading

# Base de datos simulada con información de usuarios
usuarios = {
    'juan': {'password': '1234', 'saldo': 1000.00},
    'maria': {'password': 'abcd', 'saldo': 500.00}
}

def procesar_comando(cliente, comando):
    """ Procesa los comandos enviados por el cliente """
    comando = comando.strip().split()
    if len(comando) < 1:
        return "Comando inválido. Debes proporcionar un comando válido."

    operacion = comando[0]
    monto = float(comando[1]) if len(comando) > 1 else 0.0

    if operacion == 'd':  # Depósito
        cliente['saldo'] += monto
        return f"Depósito realizado. Nuevo saldo: {cliente['saldo']:.2f}"

    elif operacion == 'r':  # Retiro
        if cliente['saldo'] >= monto:
            cliente['saldo'] -= monto
            return f"Retiro realizado. Nuevo saldo: {cliente['saldo']:.2f}"
        else:
            return "Saldo insuficiente."

    elif operacion == 'c':  # Consulta
        return f"Saldo actual: {cliente['saldo']:.2f}"

    elif operacion == 'q':  # Salir
        return "Sesión cerrada."

    else:
        return "Comando desconocido."

def manejar_cliente(cliente_socket):
    """ Maneja las conexiones de los clientes """
    cliente_socket.sendall("Introduzca su usuario: ".encode('utf-8'))
    usuario = cliente_socket.recv(1024).decode().strip()

    if usuario not in usuarios:
        cliente_socket.sendall("Usuario no válido. Conexión cerrada.\n".encode('utf-8'))
        cliente_socket.close()
        return

    cliente_socket.sendall("Introduzca su contraseña: ".encode('utf-8'))
    password = cliente_socket.recv(1024).decode().strip()

    if usuarios[usuario]['password'] != password:
        cliente_socket.sendall("Contraseña incorrecta. Conexión cerrada.\n".encode('utf-8'))
        cliente_socket.close()
        return

    cliente_socket.sendall(f"Bienvenido {usuario}! Ingrese un comando:\n".encode('utf-8'))
    cliente = usuarios[usuario]  # Recupera los datos del cliente

    while True:
        cliente_socket.sendall("cajero> ".encode('utf-8'))
        comando = cliente_socket.recv(1024).decode().strip()

        if comando == 'q':
            mensaje = "Sesión cerrada."
            cliente_socket.sendall(mensaje.encode('utf-8'))
            break

        respuesta = procesar_comando(cliente, comando)
        cliente_socket.sendall(respuesta.encode('utf-8'))

    cliente_socket.close()

def iniciar_servidor():
    """ Inicia el servidor y acepta conexiones de los clientes """
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('127.0.0.1', 12345))
    servidor.listen(5)
    print("Servidor iniciado. Esperando conexiones...")

    while True:
        cliente_socket, _ = servidor.accept()
        print("Cliente conectado.")
        cliente_thread = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
        cliente_thread.start()

if __name__ == "__main__":
    iniciar_servidor()
