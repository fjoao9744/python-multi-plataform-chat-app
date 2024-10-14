from tkinter import *
from tkinter import messagebox
from supabase import create_client

#supabase
url = "https://yurkilcutxjmzhbiojkf.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl1cmtpbGN1dHhqbXpoYmlvamtmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzgwNjM0OSwiZXhwIjoyMDQzMzgyMzQ5fQ.MqPS9cCgjrCYZACY9zQZuQsBPV98ZZCo6488Sh_wZgk"

supabase = create_client(url, key)

#tkinter
screen = Tk()
screen.geometry("800x500")

#funções
have_name = False
def name_save(event=None):
    name = name_entry.get()

    if name == "Digite seu nome..." or name == "":
        messagebox.showwarning("Nome Inválido", "Por favor, digite um nome válido.")

    else:
        name_entry.destroy()
        name_button.destroy()

        name_label.config(text=name)
        name_label.grid(row=0, column=0)
        global have_name
        have_name = True

def message_save():

    global have_name
    if have_name == True:
        message = message_entry.get()
        if message == "Digite uma mensagem..." or message == "":
            messagebox.showwarning("Mensagem Inválida", "Digite uma mensagem")

        else:
            name = name_label["text"]
            data_add = supabase.table('Mensagens').insert({"nome": name, "msg": message}).execute()

    else:
        messagebox.showwarning("Nome Inválido", "Digite um nome")

class Name_PlaceHolder():
    def view(event=None):
        if name_entry.get() == "":
            name_entry.insert(0, "Digite seu nome...")

    def clear(event=None):
        if name_entry.get() == "Digite seu nome...":
            name_entry.delete(0, "end")

class Message_PlaceHolder():
    def view(event=None):
        if message_entry.get() == "":
            message_entry.insert(0, "Digite uma mensagem...")

    def clear(event=None):
        if message_entry.get() == "Digite uma mensagem...":
            message_entry.delete(0, "end")

#   aba de entrada de nome
name_label = Label(screen)
name_entry = Entry(screen, width=40)
name_entry.grid(row=0, column=0)
name_entry.insert(0, "Digite seu nome...")
name_entry.bind("<FocusOut>", Name_PlaceHolder.view, add="+")
name_entry.bind("<FocusIn>", Name_PlaceHolder.clear, add="+")

name_button = Button(screen, text="Salvar", bg="green", command=name_save)
name_button.grid(row=0, column=1)

#aba de entrada de mensagem
message_entry = Entry(screen, width=50)
message_entry.place(x=250, y=450)
message_entry.insert(0, "Digite uma mensagem...")
message_entry.bind("<FocusOut>", Message_PlaceHolder.view, add="+")
message_entry.bind("<FocusIn>", Message_PlaceHolder.clear, add="+")

message_button = Button(screen, text="Enviar", command=message_save)
message_button.place(x=550, y=446)

#aba de mensagens recebidas
frame = Frame(screen, bg="black", width=300, height=300)
frame.place(x=50, y=50)

m = Label(frame, text="teste").grid(row=0, column=0)





mainloop()
