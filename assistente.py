import tkinter as tk
from PIL import Image, ImageTk

class JanelaComImagemFundo:
    def __init__(self, root):

        # Remover a barra de título da janela
        root.overrideredirect(True)  # Remove a barra de título

        # Definir um tamanho fixo da janela e sua posição na tela
        largura = 440
        altura = 460
        x = 1100  # Posição horizontal
        y = 100  # Posição vertical
        root.geometry(f"{largura}x{altura}+{x}+{y}")  # Largura x Altura + x + y

        # Desabilitar redimensionamento da janela
        root.resizable(False, False)  # (Horizontal, Vertical)

        # Carregar a imagem de fundo usando Pillow
        self.bg_image = Image.open("image-fundo.jpg")  # Substitua pelo caminho da sua imagem
        #self.bg_image = self.bg_image.resize((300, 200), Image.ANTIALIAS)  # Redimensionar a imagem para caber na tela
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)

        # Criar um label para exibir a imagem de fundo
        self.label = tk.Label(root, image=self.bg_image_tk)
        self.label.pack(fill="both", expand=True)  # Preencher toda a janela

        # Adicionar outros widgets sobre a imagem de fundo
        self.label_text = tk.Label(root, text="Texto sobre a imagem", bg="white", font=("Arial", 20))
        self.label_text.place(relx=0.5, rely=0.5, anchor="center")  # Centralizar o texto

        # Redimensionar a imagem conforme a janela é redimensionada
        self.label.bind("<Configure>", self.resize_image)

        # Vincular a tecla ESC ao método de fechar
        root.bind("<Escape>", self.fechar)

    def fechar(self, event):
        # Método para fechar a aplicação
        root.quit()  # Encerra o loop principal da aplicação

    def resize_image(self, event):
        # Redimensionar a imagem para caber na nova dimensão da janela
        new_width = event.width
        new_height = event.height
        resized_image = self.bg_image.resize((new_width, new_height), Image.ANTIALIAS)
        self.bg_image_tk = ImageTk.PhotoImage(resized_image)
        self.label.configure(image=self.bg_image_tk)

if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaComImagemFundo(root)
    root.mainloop()


"""
from tkinter import *
import tkinter as tk
from pynput import keyboard
from PIL import Image, ImageTk

janela = Tk()
janela.title('Assistente de jogo')
janela['background'] = 'grey25'
janela['padx'] = 20
janela['pady'] = 20
#janela['atributes'] = '-topmost', True
janela.attributes('-topmost', True)
########### teste
# Criar um canvas
janela.canvas = tk.Canvas(width=600, height=400)
janela.canvas.pack(fill="both", expand=True)

# Carregar a imagem de fundo usando Pillow
janela.bg_image = Image.open("image-fundo.jpg")  # Substitua pelo caminho da sua imagem
janela.bg_image = janela.bg_image.resize((600, 400))  # Redimensionar a imagem
janela.bg_image_tk = ImageTk.PhotoImage(janela.bg_image)

# Adicionar outros widgets sobre a imagem de fundo
janela.canvas.create_text(300, 100, text="Texto sobre a imagem", fill="white", font=("Arial", 24))

# Botão sobre a imagem
#janela.button = tk.Button(janela, text="Clique Aqui", command=janela.on_button_click)
#janela.button_window = janela.canvas.create_window(300, 200, window=janela.button)

# Adicionar a imagem de fundo ao canvas
janela.canvas.create_image(0, 0, image=janela.bg_image_tk, anchor="nw")

# FRAMES
main = Frame(janela)
menu = Frame(janela)

# VARIABLES
subjectVar = StringVar()
subjectVar.set('Pressione enter para pesquisar...')

# WIDGETS
l_title = Label(main, text='Assistente de Atalhos')

l_subject = Label(main, text='Sair - Esc')
e_subject = Entry(main, textvariable=subjectVar)

l_results = Label(main, text='Menu - Ctrl + M')
lb_news = Listbox(main)

##########################
# testes

###########################3

# CUSTOMIZATION
main['background'] = 'grey25'
menu['background'] = 'grey25'

l_title['font'] = ('Roboto Slab', 20, 'bold')
l_title['bg'] = 'grey25'
l_title['fg'] = 'grey99'
l_subject['font'] = ('Roboto Slab', 10)
l_subject['bg'] = 'grey25'
l_subject['fg'] = 'grey99'
e_subject['font'] = ('Roboto Slab', 12)
e_subject['bg'] = 'grey25'
e_subject['fg'] = 'grey99'
e_subject['width'] = 100

l_results['font'] = ('Roboto Slab', 10)
l_results['bg'] = 'grey25'
l_results['fg'] = 'grey99'
lb_news['font'] = ('Roboto Slab', 12)
lb_news['bg'] = 'grey25'
lb_news['fg'] = 'grey99'
lb_news['width'] = 100



# POSITION
main.pack()
menu.pack()

l_title.pack(pady=(5,10))
l_subject.pack(anchor=W, pady=(5,2))
e_subject.pack(pady=(5,10))


def on_press(key):
    if key == keyboard.Key.esc:
        janela.tk.quit()
        
        print('etste')
        return False  # Encerra o programa
        
        exit    
        

    print('Tecla pressionada:', key)

# Cria um listener para capturar os eventos de teclado
listener = keyboard.Listener(on_press=on_press)
listener.start()

janela.mainloop()
# Mantém o programa em execução até que a tecla Esc seja pressionada
listener.join()
#from backend import *


# NOTAS
#link para compilar em .EXE= https://www.youtube.com/watch?v=Kp_41haOVQk
"""