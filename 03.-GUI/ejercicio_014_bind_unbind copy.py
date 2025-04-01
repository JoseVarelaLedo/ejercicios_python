import tkinter as tk
from tkinter import messagebox as msgbox

main_window = tk.Tk() 
main_window.title('Ejemplo bind / unbind')
main_window.geometry('400x300')

def desvincular (event):
    label.unbind('<Button-1>') # Desvinculamos el evento
    label['text']='Ya no'
    msgbox.showinfo('Ejemplo', 'Botón desvinculado')
    
label = tk.Label(main_window, text='Púlsame')
label.bind('<Button-1>', desvincular) # Pulsar con el ratón
label.pack()

main_window.mainloop()