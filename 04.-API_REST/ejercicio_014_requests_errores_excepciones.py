import requests as req

try:
    reply = req.get('http://localhost:3000', timeout=0.1) 
except req.exceptions.InvalidURL as iurl:
    # La URL está mal construida
    print ('InvalidURL:',iurl)
except req.exceptions.Timeout as to:
    # Error por el tiempo de respuesta (hay que capturar antes que ConnectionError, por jerarquía de excepciones)
    print ('Timeout:', to)
except req.exceptions.ConnectionError as ce:
    # Error de conexión (p.ej. servidor frito)
    print ('ConnectionError:', ce)
else:
    print (reply.status_code)
finally:
    print ('Fin de ejecución')
