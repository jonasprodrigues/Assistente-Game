from tkinter import *
from pynput import keyboard


janela = Tk()
janela.title('Assistente de jogo')
janela['background'] = 'grey25'
janela['padx'] = 20
janela['pady'] = 20
#janela['atributes'] = '-topmost', True
janela.attributes('-topmost', True)

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

###########################

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