# IPv4: 32 bits     192.168.1.138  Se forman con cuatro grupos de dígitos: 0-255.0-255.0.255-0.255
# IPv6: 128 bits    2001:0db8:85a3:0000:0000:8a2e:0370:7334. 

# Pasos para crear un socket cliente:
#   1.- Crear el socket (instancia de la clase socket)
#   2.- Establecer la conexión: método connect()
#   3.- Envío de solicitud al servidor: método send()
#   4.- Recibimos respuesta del servidor: método recv()
#   5.- Cerrar socket: métodos shutdown() y close()

import socket

# Normalmente se definirían constantes
# SERVER_ADDRESS
# IP_ADDRESS

# En este caso pedimos al usuario los datos

server_address = input ('Host IP:')
server_ip_address = int(input('Host Port:'))

# 1.- Crear el socket
# AF_INET --> el socket se basa en DIRECCION + PUERTO
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP, si queremos UDP es SOCK_DGRAM para datagramas

# 2.- Establecer la conexión
socket_cliente.connect((server_address, server_ip_address)) # MUCHO OJO, SE PASA UNA TUPLA COMO ARGUMENTO, QUE REFERENCIA UN OBJETO DE LA CLASE ADDRESS

# 3.-Enviar solicitud
socket_cliente.send(b"GET / HTTP/1.1\r\nHost: "
                    + bytes(server_address, "utf8")
                    + b"\r\nConnection: close\r\n\r\n")

# 4.- Recibir respuesta:
# El argumento es el tamaño del buffer de bytes
respuesta = socket_cliente.recv(1000) 

# 5.- Cierre de sockets:
# Constantes posibles para método shutdown:
#   - SHUT_RDWR --> Dejamos de leer y escribir
#   - SHUD_RD   --> Dejamos de leer
#   - SHUT_WR   --> Dejamos de escribir
socket_cliente.shutdown(socket.SHUT_RDWR)
socket_cliente.close()

# Tratar la respuesta del servidor
print(repr(respuesta))