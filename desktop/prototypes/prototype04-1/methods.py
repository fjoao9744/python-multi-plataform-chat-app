import tkinter as tk
import threading as th
from connect import Connection

class MessageList:
    def __init__(self, screen):
        self.list = tk.Listbox(screen)
        self.list.pack()
        
        conn = Connection()
        
        for message in conn.show_all_messages():
            self.add_message(message)
            
        self.last_message_id = message["id"]
            
    def size(self, new_height, new_wight):
        self.list.config(width= new_wight, height= new_height)
    
    def add_message(self, message):
            self.list.insert(tk.END, f"{message["nome"]} - {message["mensagem"]}")
    
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

