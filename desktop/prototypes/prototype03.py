from tkinter import *

# Configurações da tela
screen = Tk()
screen.geometry("300x400")
screen.config(bg="#2B2B33")
screen.title("Chat Online")


# Aba de inserção do nome

def name_save(event=None):

    name = name_entry.get()
    name_button["state"] = DISABLED

    name_entry.config(state='disabled')
    name_entry.config(bg="#2B2B33", relief=FLAT )
    

name_button = Button(screen, text="save", bg="#2D2B41", relief=SOLID, fg='#C2CDE9', font=("Courier", 12), command=name_save)
name_entry = Entry(screen, bg="#39366B", relief=SOLID, bd=2, fg='#C2CDE9', font=("Courier", 12))




name_entry.pack(padx=(10, 0), pady=5, anchor=N, side=LEFT, ipady=3)
name_button.pack(padx=10, pady=4, anchor=N, side=LEFT)

mainloop()