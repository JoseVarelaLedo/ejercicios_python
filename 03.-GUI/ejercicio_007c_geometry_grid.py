import tkinter as tk

main_window = tk.Tk() 

main_window.title('Ejemplo grid')
main_window.geometry('800x600')

# La cuadrícula no es visible, es sólo de diseño
# Las filas tienen el mismo alto (con precauciones)
# Las columnas tienen el mismo ancho
# No se indican ni el número de filas ni el de columnas, se infieren por el rango que damos

# label = tk.Label(main_window, text='Nombre')
boton_1 = tk.Button(main_window, text='Botón 1')
boton_2 = tk.Button(main_window, text='Botón 2')
boton_3 = tk.Button(main_window, text='Botón 3')
boton_4 = tk.Button(main_window, text='Botón 4')

boton_1.grid (column=0, row=0, columnspan=4, sticky='ew') # Debería expandir el botón
boton_2.grid (column=1, row=4)
boton_3.grid (column=2, row=2)
boton_4.grid (column=3, row=2)

main_window.mainloop()