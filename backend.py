
from tkinter import *
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # Encerra o programa

    print('Tecla pressionada:', key)

# Cria um listener para capturar os eventos de teclado
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Mantém o programa em execução até que a tecla Esc seja pressionada
listener.join()