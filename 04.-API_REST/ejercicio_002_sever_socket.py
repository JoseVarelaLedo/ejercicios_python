# SOCKET DE SERVIDOR
import socket

# Para los server sockets es necesario indicar dónde y cómo, es decir, ip y puerto
host = '127.0.0.1' # localhost
port = 8021 # puerto de escucha

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignar servidor y puerto al socket
socket_server.bind((host, port)) # TUPLA

# Ponemos al servidor a la escucha
socket_server.listen()
print (f'Servidor {host} escuchando en puerto {port}')

# Indicar al socket_server que acepte paquetes de datos
socket_client, direccion_cliente = socket_server.accept() # devuelve una TUPLA con el canal o socket del cliente y su dirección

print (f'Recibida petición del cliente {socket_client} desde {direccion_cliente}')

# Recoger los datos
datos = socket_client.recv(1024) # Buffer de bytes
print (f'Datos recibidos: {datos.decode('utf-8')}')

# Envío de respuesta
mensaje = 'Hola, soy el servidor'
socket_client.send (mensaje.encode('utf-8'))
print(f'Se ha enviado al cliente el siguiente mensaje: "{mensaje}"')