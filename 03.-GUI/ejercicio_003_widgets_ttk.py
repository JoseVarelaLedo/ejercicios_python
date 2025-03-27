from tkinter import ttk # Módulo para asignar estilos

import tkinter as tk
import tkinter.messagebox as msgbox 


main_window = tk.Tk() 

main_window.title('Mi APP TkInter')

main_window.geometry('800x600')

boton_tk = tk.Button (main_window, text='Botón tk')
boton_ttk = ttk.Button (main_window, text='Botón ttk')

boton_tk.pack()
boton_ttk.pack()

main_window.mainloop()  