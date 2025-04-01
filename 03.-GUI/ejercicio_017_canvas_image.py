import tkinter as tk
from tkinter import ttk

# El avance se hará pulsando una tecla
# La velocidad será un atributo de Posicion
# La imagen no debe dar rastro

DEFAULT_SPEED = 10
PICTURE = 'totoro.png'
TAG_IMAGE = 'image'

class Posicion:
    def __init__(self, x, y, velocidad=DEFAULT_SPEED):
        self.x = x
        self.y = y
        self.velocidad = velocidad

def move(canvas : tk.Canvas, posicion : Posicion):
    posicion.x+=posicion.velocidad
    canvas.delete(TAG_IMAGE)
    canvas.create_image(posicion.x, 200, image=image, tags=TAG_IMAGE)

window = tk.Tk()
window.title('Mover a Totoro')

canvas = tk.Canvas(window, width=400, height=400, bg='cyan')

image = tk.PhotoImage(file=PICTURE)

button_quit = ttk.Button(window, text='Quit',command=window.destroy)

# Posición inicial, luego se va modificando, dejamos la velocidad por defecto
position = Posicion(-75, 200)
button_mover = ttk.Button(window, text='Move',
    command = lambda canvas_parametro=canvas, posicion_parametro=position : 
        move(canvas_parametro, posicion_parametro))

canvas.create_image(position.x, 200, image=image, tags=TAG_IMAGE)
window.bind("<space>", lambda event: move(canvas, position))

canvas.grid(row=0)
button_quit.grid(row=1)
button_mover.grid(row=2)
window.mainloop()
