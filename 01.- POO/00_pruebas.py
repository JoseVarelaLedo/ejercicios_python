import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Has presionado Ctrl+M!")

def salir():
    window.quit()

window = tk.Tk()
window.title("Ejemplo de Aceleradores")

# Crear menú
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Mensaje", command=mostrar_mensaje, accelerator="Ctrl+M")
file_menu.add_separator()
file_menu.add_command(label="Salir", command=salir, accelerator="Ctrl+Q")

menu_bar.add_cascade(label="Archivo", menu=file_menu)

# Asignar aceleradores (atajos de teclado)
window.bind("<Control-m>", lambda event: mostrar_mensaje())
window.bind("<Control-q>", lambda event: salir())

window.mainloop()
