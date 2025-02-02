import tkinter as tk

class MessageList:
    def __init__(self, screen):
        self.list = tk.Listbox(screen)
        self.list.pack()
        
    def size(self, new_height, new_wight):
        self.list.config(width= new_wight, height= new_height)
        
        
class Send:
    class Button:
        def __init__(self, screen):
            self.button = tk.Button(screen, text="send")
            self.button.pack()
    class Input:
        def __init__(self, screen):
            self.button = tk.Entry(screen)
            self.button.pack()
