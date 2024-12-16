from tkinter import *
from methods import *

import asyncio

def chat_screen(event=None):
    
    screen = Tk()

    screen.state("zoomed")
    screen.title("Chat online")

    mainloop()
        
def login_screen(event=None):
    screen = Tk()
    screen.geometry("300x400")
    screen.title("Login")
    name = Entry_(screen, "Digite seu nome")
    name.pack(pady=30)
    email = Entry_(screen, "Digite seu email")
    email.pack(pady=(0, 30))


    entrar_button = Button(screen, text="entrar", command=chat_screen) # Alterar o nome mais tarde
    entrar_button.pack()

    mainloop()

login_screen()
