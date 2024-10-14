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

def message_save(event=None):
    global have_name
    if have_name == True:
        message = message_entry.get()
        message_entry.delete(0, "end")
        if message == "Digite uma mensagem..." or message == "":
            messagebox.showwarning("Mensagem Inválida", "Digite uma mensagem")

        else:
            name = name_label["text"]
            data_add = supabase.table('Mensagens').insert({"nome": name, "msg": message}).execute()
            update_messages()
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

def update_messages(event=None):
    global last_message
    messages = supabase.table('Mensagens').select('*').execute()
    messages_list = messages.data
    new_messages = messages_list[last_message:]

    print(messages_list[last_message], messages_list[-1])
    if messages_list[last_message] == messages_list[-1]:
        pass
    else:   
        last_message = messages_list.index(messages_list[-1])
        for index, _ in enumerate(new_messages):
            if index != 0:
                messages_received.insert(END, f"{_["nome"]} - {_["msg"]}")

    messages_received.see(END)

#   aba de entrada de nome
name_label = Label(screen)
name_entry = Entry(screen, width=40)
name_entry.grid(row=0, column=0)
name_entry.insert(0, "Digite seu nome...")
name_entry.bind("<FocusOut>", Name_PlaceHolder.view, add="+")
name_entry.bind("<FocusIn>", Name_PlaceHolder.clear, add="+")
name_entry.bind("<Return>", name_save, add="+")


name_button = Button(screen, text="Salvar", bg="green", command=name_save)
name_button.grid(row=0, column=1)

#aba de entrada de mensagem
message_entry = Entry(screen, width=50)
message_entry.place(x=250, y=450)
message_entry.insert(0, "Digite uma mensagem...")
message_entry.bind("<FocusOut>", Message_PlaceHolder.view, add="+")
message_entry.bind("<FocusIn>", Message_PlaceHolder.clear, add="+")
message_entry.bind("<Return>", message_save, add="+")

message_button = Button(screen, text="Enviar", command=message_save)
message_button.place(x=550, y=446)

#aba de mensagens recebidas
messages_received = Listbox(screen, height=20, width=120)
messages_received.place(x=50, y=50)

message_label = Label(screen, text="Mensagens:", font=("Arial", 16)).place(x=50, y=40)

messages = supabase.table('Mensagens').select('*').execute()
for _ in messages.data:
    messages_received.insert(END, f"{_["nome"]} - {_["msg"]}")
 
messages_list = messages.data
last_message = messages_list.index(messages_list[-1])

#botao de atualizar
messages_update_button = Button(screen, text="Atualizar", command=update_messages)
messages_update_button.place(x=592, y=446)

mainloop()
