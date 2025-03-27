import tkinter as tk

main_window = tk.Tk() 

main_window.title('Mi APP TkInter')
main_window.geometry('400x300')

boton_1 = tk.Button (main_window, text='1', width=5, height=3)
boton_2 = tk.Button (main_window, text='2', width=5, height=3)

boton_1.grid (row=0, column=0)
boton_2.grid (row=0, column=2)

main_window.mainloop()  