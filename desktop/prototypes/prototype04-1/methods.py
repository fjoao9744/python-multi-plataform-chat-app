import tkinter as tk
from connect import Connection

class MessageList:
    def __init__(self, screen):
        self.list = tk.Listbox(screen)
        self.list.pack()
        
    def size(self, new_height, new_wight):
        self.list.config(width= new_wight, height= new_height)
        
class Send:
    class Button:
        def __init__(self, screen):
            self.button = tk.Button(screen, text="send", command=self.send)
            self.button.pack()
            
        def send(self):
            mensagem = self.input.entry.get()
            data = {
                "nome": "teste",
                "mensagem": mensagem
            }
            
            conn = Connection()
            
            conn.send_message(data)
            
        def input_define(self, input):
            self.input = input
        
    class Input:
        def __init__(self, screen):
            self.entry = tk.Entry(screen)
            self.entry.pack()

