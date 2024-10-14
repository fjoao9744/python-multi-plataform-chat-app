from tkinter import *
from supabase import create_client

url = "https://yurkilcutxjmzhbiojkf.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl1cmtpbGN1dHhqbXpoYmlvamtmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzgwNjM0OSwiZXhwIjoyMDQzMzgyMzQ5fQ.MqPS9cCgjrCYZACY9zQZuQsBPV98ZZCo6488Sh_wZgk"

screen = Tk()
screen.geometry("800x500")

def name_save(event=None):
    name = name_entry.get()
    name_entry.destroy()
    name_button.destroy()

class Name_PlaceHolder():
    def view(event=None):
        if name_entry.get() == "":
            name_entry.insert(0, "Digite seu nome...")

    def clear(event=None):
        if name_entry.get() == "Digite seu nome...":
            name_entry.delete(0, "end")

#   aba de entrada de nome
name_entry = Entry(screen, width=40)
name_entry.grid(row=0, column=0)
name_entry.insert(0, "Digite seu nome...")
name_entry.bind("<FocusOut>", Name_PlaceHolder.view, add="+")
name_entry.bind("<FocusIn>", Name_PlaceHolder.clear, add="+")

name_button = Button(screen, text="salvar nome", bg="green", command=name_save)
name_button.grid(row=0, column=1)

#aba de entrada de mensagem
msg_entry = Entry(screen, width=40)
msg_entry.grid(row=1, column=0)

print(name_entry.get())



mainloop()
