''' Importações '''
from tkinter import *


''' Caixa de Entrada '''
class Entry_:
    def __init__(self, screen, placeholder = ""):
        # Cria e posiciona o botão
        self.__entry = Entry(screen)
        self.__entry.pack()

        # Configurações do placeholder
        self.placeholder = placeholder 
        self.__switch_placeholder(None) # inicia a função
        self.__entry.bind("<FocusIn>", self.__switch_placeholder)
        self.__entry.bind("<FocusOut>", self.__switch_placeholder)

        # A cor padrão do texto
        self.text_color = "black"

        # Indicador se tem algum texto ou não
        self.is_text = False

    # Função que vai ativar e desativar o placeholder
    def __switch_placeholder(self, event):
        if self.__entry.get() != self.placeholder:
            self.is_text = True

        if self.__entry.get() == self.placeholder: 
            self.__entry.delete(0, "end") # Se o usuario clicar apaga tudo
            self.__entry.config(fg = self.text_color) # Se o usuario clicar volta a cor ao normal
            return

        if self.__entry.get() == "":
            self.__entry.insert(0, self.placeholder) # Se o usuario tirar o mouse uma mensagem vai aparecer
            self.__entry.config(fg = "grey") # A cor da mensagem vai ser cinza
            return

    def __call__(self, *args, **kwargs): # Se você só chamar o objeto você consegue usar o .config
        self.__entry.config(*args, **kwargs)

    def pack(self, **kwargs): # Sobrescrevendo o pack
        self.__entry.pack(kwargs)

    def get(self):
        return self.__entry.get()
    
    def text(self, text):
        self.__entry.delete(0, "end")
        self.__entry.insert(0, text)
        self.__entry.config(fg = "black")

            

            

            