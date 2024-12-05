from tkinter import *
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

    entrar_button = Button(screen, text="entrar", command=chat_screen) # Alterar o nome mais tarde
    entrar_button.pack()

    mainloop()

login_screen()
