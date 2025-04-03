import requests as req

reply = req.get('http://localhost:3000') # Petición HTTP GET

# ##########################################
# Código de control de HTTP: status_code
# ##########################################
status_code = reply.status_code # Código HTTP de la respuesta

print (status_code) # 200

if status_code == 200:
    print ('Ok')

# Equivalente a lo de arriba con cadenas del diccionario asociado a requests
if status_code == req.codes.OK: # tb hay "ok", "okay", "all_ok", "all_okay", "all_good", "\\o/", "✓"
    print('Ok')
    
# ##########################################
# Código de control de HTTP: response
# ##########################################
response = reply.text # imprime el código html
    

