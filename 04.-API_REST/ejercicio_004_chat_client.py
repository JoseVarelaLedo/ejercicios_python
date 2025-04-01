# CLiente Chat
import socket

HOST_IP = '127.0.0.1'
HOST_PORT = 8021
CORTOCIRCUITO = 'VAIVAI'

# Creamos el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST_IP, HOST_PORT))

while True:
    # Intercambio de mensajes mientras no se teclee la expresión de cortocircuito
    mensaje = input('Cliente: ')  
    sock.send(mensaje.encode('utf-8'))
    
    if mensaje.upper() == CORTOCIRCUITO:  
        break
   
    respuesta = sock.recv(1024).decode('utf-8')
    print(f'Servidor: {respuesta}')

    if respuesta.upper() == CORTOCIRCUITO:  
        break

sock.shutdown(socket.SHUT_RDWR)
sock.close()
