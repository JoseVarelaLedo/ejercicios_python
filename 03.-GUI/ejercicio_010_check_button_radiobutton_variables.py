import tkinter as tk

main_window = tk.Tk() 
main_window.title('Ejemplo variables')
main_window.geometry('400x300')

def mostrar():
    print ('Mostrando...')
    print (intercambio.get()) # Obtenemos el valor de la variable intercambio

# Declaración especial de la variable compartida, que es un objeto especial de TkInter
# Permite comunicación entre los diferentes componentes
# Existen IntVar, DoubleVar, BooleanVar, StringVar
intercambio = tk.BooleanVar() # Declaración de variable compartida
intercambio.set(True) # Asignación

# Existen otros tipos
# tk.DoubleVar()
# tk.BooleanVar()
# tk.StringVar()

checkbutton_1 = tk.Checkbutton (main_window, text='Seleccionar esta opción', variable=intercambio)
checkbutton_2 = tk.Checkbutton (main_window, text='Seleccionar esta otra opción')
radiobutton_1 = tk.Radiobutton (main_window, text='Opcion 1', value=True, variable=intercambio)
radiobutton_2 = tk.Radiobutton (main_window, text='Opcion 2', value=False, variable=intercambio)

button = tk.Button (main_window, text = 'Pulsa', command=mostrar)

checkbutton_1.pack()
checkbutton_2.pack()
radiobutton_1.pack()
radiobutton_2.pack()
button.pack()

main_window.mainloop()