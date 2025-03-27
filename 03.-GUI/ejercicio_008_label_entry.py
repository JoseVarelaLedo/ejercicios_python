import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox 

# Crear un interfaz que solicite el título de una película
# Cuando se pulsa un botón:
#   - valida si hay API_KEY
#   - valida que hay algo en el widget entry
# Si no hay nada usamos un messagebox de error
# Si hay algo llamamos una función que muestra el texto escrito
# Además se va a solicitar una API_KEY (clave de acceso) junto con un botón guardar

main_window = tk.Tk() 
main_window.title('Interfaz películas')
main_window.geometry('400x300')

api_key = ['']  

def save_api_key():    
    clave = api_entry.get().strip()
    if clave == '':
        msgbox.showerror('Error', 'Debes introducir una API_KEY')
    else:
        api_key[0] = clave
        msgbox.showinfo('Éxito', 'API_KEY guardada correctamente')

def validate():    
    if api_key[0] == '':
        msgbox.showerror('Error', 'No hay API_KEY guardada')
        return

    titulo = titulo_entry.get().strip()
    if titulo == '':
        msgbox.showerror('Error', 'No has introducido el título de la película')
        return

    msgbox.showinfo('Película', f'Has introducido: {titulo}')

api_label = tk.Label(main_window, text='Introduce API_KEY')
api_entry = ttk.Entry(main_window, width=20)
guardar_button = ttk.Button(main_window, text='Guardar API_KEY', command=save_api_key)
titulo_label = tk.Label(main_window, text='Introduce el título de la película')
titulo_entry = ttk.Entry(main_window, width=20)
validar_button = ttk.Button(main_window, text='Validar', command=validate)

api_label.place(x=150, y=50)
api_entry.place(x=150, y=80)
guardar_button.place(x=150, y=110)
titulo_label.place(x=150, y=160)
titulo_entry.place(x=150, y=190)
validar_button.place(x=150, y=220)

main_window.mainloop()