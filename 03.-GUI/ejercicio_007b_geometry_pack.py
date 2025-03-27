import tkinter as tk

main_window = tk.Tk() 

main_window.title('Ejemplo pack')
main_window.geometry('800x600')


# label = tk.Label(main_window, text='Nombre')
boton_1 = tk.Button(main_window, text='Botón 1')
boton_2 = tk.Button(main_window, text='Botón 2')
boton_3 = tk.Button(main_window, text='Botón 3')
boton_4 = tk.Button(main_window, text='Botón 4')

# La posición se autoajusta al tamaño de la ventana
boton_1.pack ()
boton_2.pack ()
boton_3.pack ()
# usamos una constante propia de tkinter para el posicionamiento en el fondo
# y con fill rellena todo el espacio
boton_4.pack (side=tk.BOTTOM, fill=tk.X) 

main_window.mainloop()