import tkinter as tk
import tkinter.messagebox as msgbox 

main_window = tk.Tk() 
main_window.title('Ejemplo bind')
main_window.geometry('400x300')

def saludar(event):
    msgbox.showinfo('Saludador', 'Hola!')
    print (type(event))
    print (event)
    
label = tk.Label (main_window, text='Púlsame')

# Utilizamos la función bind para asociar un evento a la etiqueta label
label.bind('<Button-1>', saludar) # Pulsar con el ratón
label.bind('<Enter>', lambda evento: print ('Entrando')) # Mouse over
label.bind('<Leave>', lambda evento: print ('Saliendo')) # Mouse Leave
label.pack()

main_window.mainloop()