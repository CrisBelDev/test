import socket

def iniciar_cliente():
    """ Inicia el cliente que se conecta al servidor """
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("127.0.0.1", 12345))

    while True:
        # Recibe la bienvenida o error de credenciales
        mensaje = cliente.recv(1024).decode()
        print(mensaje, end="")

        # Si es el login, el usuario introduce sus credenciales
        if "Introduzca su usuario:" in mensaje:
            usuario = input()
            cliente.sendall(usuario.encode('utf-8'))
        elif "Introduzca su contraseña:" in mensaje:
            password = input()
            cliente.sendall(password.encode('utf-8'))

        # Si el login es exitoso, permite realizar acciones
        if "Ingrese un comando:" in mensaje:
            while True:
                comando = input("cajero> ").strip()
                if comando:
                    cliente.sendall(comando.encode('utf-8'))

                    # Recibe la respuesta del servidor
                    respuesta = cliente.recv(1024).decode()
                    print(respuesta)

                    if "Sesión cerrada" in respuesta:
                        print("Cerrando sesión...")
                        break  # Sale del bucle del cajero

                else:
                    print("Comando vacío, por favor ingrese un comando válido.")

            break  # Sale del bucle del login y cierra la conexión

    cliente.close()  # Cierra la conexión del cliente cuando se sale

if __name__ == "__main__":
    iniciar_cliente()
