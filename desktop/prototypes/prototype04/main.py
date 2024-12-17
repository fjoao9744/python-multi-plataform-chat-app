from tkinter import *
from tkinter import messagebox
from methods import *
from connection import *

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

    def login(event=None):
        login = Login(user = {"name": name_entry.get(), "login": login_entry.get(), "password": senha_entry.get()})
        if login.execute():
            entrar_button.config(state= NORMAL)
        else:
            messagebox.showinfo("login incorreto", "O login esta incorreto") # mudar isso mais tarde


    name_entry = Entry_(screen, "Digite seu nome")
    name_entry.pack(pady=30)

    login_entry = Entry_(screen, "Digite seu login")

    senha_entry = Entry_(screen, "Digite sua senha")
    senha_entry.pack(pady=30)

    entrar_button = Button(screen, text="entrar", command= lambda: (screen.state("withdrawn"), chat_screen()), state=DISABLED) # Alterar o nome mais tarde
    entrar_button.pack()

    register_button = Button(screen)
    register_button.pack()

    login_button = Button(screen, text="Login", command=login)
    login_button.pack()


    mainloop()


login_screen()
