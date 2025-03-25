# Hola Mundo en TkInter

# Paso 1: hacer las importaciones
import tkinter as tk
import tkinter.messagebox as msgbox # Mensajes flotantes o emergentes

# Paso 2: hacer la ventana principal
main_window = tk.Tk()   # Ventana

# Paso 3: asignar un título
main_window.title('Mi APP TkInter')

# Paso 4: ajustar tamaño ventana
main_window.geometry('800x600')

# Paso 5: añadir componentes (primero un botón)
boton_saludar = tk.Button (main_window, text='Saluda', width=10, height=3, 
                                            #command=lambda:print('Hola Mundo!')
                                            command=lambda: msgbox.showinfo('Saludo', 'Hola Mundo'))

# boton_saludar.pack() # necesario para que el componente se incluya en la ventana; es el modo más automático, centrado y arriba

boton_saludar.place (x=400, y=300) # otro modo, colocando en coordenadas cartesianas, en este caso en el centro (dada la resolución)

# existe otra forma de posicionar, grid(), que ubica los componentes en una malla o parrilla


# Paso 6: añadir otro botón para salir
def salir():
    # Paso 7, añadir messagebox para comprobar la salida de la aplicación
    respuesta = msgbox.askquestion('Salir', '¿Estás seguro de querer salir?')
    if respuesta == 'yes':
        main_window.destroy() # Finaliza la aplicación
    else:
        print (respuesta)
        
boton_salir = tk.Button (main_window, text='Salir', width=10, height=3, command=salir)

boton_salir.place(x=400, y=400)

main_window.mainloop()  # Bucle de ejecución. La app no puede parar. Hay que poner esta línea al final