import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox 

main_window = tk.Tk() 
main_window.title('Ejemplo colores')
main_window.geometry('400x300')

# bg -- background
# fg -- foreground
# activebackground
# activeforeground

# RGB   RED   GREEN  BLUE (0,255) o 2 elevado a 8 posibilidades
# blue  #00    00     FF

button_save_api_key = tk.Button(main_window, text='Guardar', width=10, height=10, bg= 'red', fg='white', activebackground='beige', activeforeground='red')

button_save_api_key.pack()

main_window.mainloop()