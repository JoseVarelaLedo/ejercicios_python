import requests as req
            
try:
    reply = req.get('http://localhost:3000/movies', timeout=0.1) 
except req.exceptions.ConnectionError as ce:   
    print ('ConnectionError:', ce)
except Exception as e:
    print ('Exception', e)    
else:
    if reply.status_code==req.codes.OK:
        movies = reply.json()
        print (type(movies))
        print(movies)
    else:
        print('Ha pasado algo que impide la ejecución esperada:', reply.status_code)
finally:
    print ('Fin de ejecución')