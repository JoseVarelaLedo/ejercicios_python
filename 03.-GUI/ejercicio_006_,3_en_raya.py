import tkinter as tk
import tkinter.messagebox as msgbox 

main_window = tk.Tk()
main_window.title('3 En Raya')
main_window.geometry('290x350')

turno = ['X']  
botones = []

def switch(button):
    if button['text'] == 'X' or button['text'] == 'O': 
        msgbox.showinfo('Casilla ya usada', 'Pulsa sobre otra casilla')
        return
    button.config(text=turno[0])
    if check_winner(turno[0]):  # Verificar si el jugador actual ha ganado
        msgbox.showinfo('¡Fin del juego!', f'¡El jugador con {turno[0]} ha ganado!')
        reset()
        return
    turno[0] = 'O' if turno[0] == 'X' else 'X'  # Cambiar turno

def check_winner(player):
    """Verifica si el jugador actual ha ganado."""
    # Comprobar filas y columnas
    for i in range(3):
        if all(botones[i][j]['text'] == player for j in range(3)):  # Fila completa
            return True
        if all(botones[j][i]['text'] == player for j in range(3)):  # Columna completa
            return True

    # Comprobar diagonales
    if all(botones[i][i]['text'] == player for i in range(3)):  # Diagonal principal
        return True
    if all(botones[i][2-i]['text'] == player for i in range(3)):  # Diagonal inversa
        return True

    return False  # No hay ganador aún

def reset():
    """Pregunta si se desea reiniciar y borra el tablero si la respuesta es afirmativa."""
    respuesta = msgbox.askyesno('Reiniciar', '¿Quieres reiniciar la partida?')
    if respuesta:  # Solo reinicia si el usuario responde "Sí"
        for fila in botones:
            for boton in fila:
                boton.config(text='')  # Vaciar casillas

# Crear los botones del tablero
for row_index in range(3):  
    fila = []
    for column_index in range(3):  
        boton = tk.Button(main_window, text='', width=10, height=5, padx=10)
        boton.config(command=lambda b=boton: switch(b))          
        boton.grid(row=row_index, column=column_index)
        fila.append(boton)
    botones.append(fila)

# Botón para reiniciar
boton_reset = tk.Button(main_window, text='Reiniciar partida', width=20, height=3, command=reset)
boton_reset.grid(row=3, column=0, columnspan=3)

main_window.mainloop()
