from tkinter import *
from funcs import *

# Configurações da tela
screen = Tk()
screen.geometry("300x400")
screen.config(bg="#2B2B33")
screen.title("Chat Online")

# Aba de inserção do nome
name_button = Button(screen, text="save", bg="#2D2B41", relief=SOLID, fg='#C2CDE9', font=("Courier", 12))
name_entry = Entry(screen, bg="#39366B", relief=SOLID, bd=2, fg='#C2CDE9', font=("Courier", 12))




name_entry.pack(padx=(10, 0), pady=5, anchor=N, side=LEFT, ipady=3)
name_button.pack(padx=10, pady=4, anchor=N, side=LEFT)

mainloop()