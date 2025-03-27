import tkinter as tk

main_window = tk.Tk() 
main_window.title('Ejemplo place')
main_window.geometry('800x600')

# label = tk.Label(main_window, text='Nombre')
boton = tk.Button(main_window, text='Calcular')

boton.place(x=100, y=50) # alto y ancho en píxeles

main_window.mainloop()