# Servidor chat
import socket

SERVER_HOST = '127.0.0.1' 
SERVER_PORT = 8021 
CORTOCIRCUITO = 'VAIVAI'

# Creación del socket
sock_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_servidor.bind((SERVER_HOST, SERVER_PORT))
sock_servidor.listen()

print(f'Servidor {SERVER_HOST} escuchando en el puerto {SERVER_PORT}')
socket_cliente, direccion_cliente = sock_servidor.accept()
print(f'Se ha recibido una petición desde {direccion_cliente}')

while True:
    # Aceptar mensajes de cliente mientras no envíe el mensaje "prohibido"
    datos = socket_cliente.recv(1024).decode('utf-8')
    print(f'Cliente: {datos}')

    if datos.upper() == CORTOCIRCUITO:  
        break
  
    mensaje = input('Servidor: ') 
    socket_cliente.send(mensaje.encode('utf-8'))

    if mensaje.upper() == CORTOCIRCUITO: 
        break

socket_cliente.close()
sock_servidor.close()
