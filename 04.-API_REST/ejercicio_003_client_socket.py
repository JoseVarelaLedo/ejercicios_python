# SOCKET DE CLIENTE
import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8021 

# Creamos socket
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Indicamos dirección y puerto
socket_cliente.connect((SERVER_ADDRESS, SERVER_PORT))

# Envío de mensaje
mensaje = 'Hola, soy el cliente'
socket_cliente.send(mensaje.encode('utf-8'))
print (f'Enviando al servidor el mensaje: {mensaje}')

# Lectura de respuesta
respuesta = socket_cliente.recv(1000) 

print(f'Recibiendo el mensaje {respuesta.decode('utf-8')} procedente del servidor')

# Cierre
socket_cliente.shutdown(socket.SHUT_RDWR)
socket_cliente.close()