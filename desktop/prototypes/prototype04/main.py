
from methods import *
from connection import *
from tkinter import *
from tkinter import messagebox

def chat_screen(event=None):
    
    screen = Tk()

    screen.state("zoomed")
    screen.title("Chat online")
    
    remember = RememberMe(user = None)

    name_user_label = Label(screen, text=remember.show_name(), font=("Arial", 20))
    name_user_label.place(x=0, y=0)
    
    messagelist = Listbox(screen, width=250, height=40)
    
    add_messages(messagelist)
    
    messagelist.pack(pady=50)
    
    message_entry = Entry_(screen, placeholder="Digite sua mensagem aqui")
    message_entry.pack()
    def message_get():
        message = {"nome": name_user_label['text'],"mensagem": message_entry.get()}
        
        return message
    
    connect = Connection()
    message = message_get()
    
    message_send_button = Button(screen, text="Enviar mensagem", command=connect.send_message(message))
    message_send_button.pack()

    mainloop()

def login_screen(event=None):
    screen = Tk()
    screen.geometry("300x400")
    screen.title("Login")

    def login(event=None):
        if senha_entry.get() == "Digite sua senha" or login_entry.get() == "Digite seu login":
            messagebox.showinfo("Digite um login", "digite um login e uma senha para poder prossegir")
            return

        if senha_entry.get() == "" or login_entry.get() == "":
            messagebox.showinfo("Digite um login", "digite um login e uma senha para poder prossegir")
            return

        usuario = {
            "name": name_entry.get(), 
            "login": login_entry.get(), 
            "password": senha_entry.get()
            }

        login = Login(user = usuario)
        login_user = login.execute()
        remember = RememberMe(login_user)
        
        if login_user == False:
            messagebox.showinfo("login incorreto", "Por favor, digite um login e uma senha valida")

        elif login_user["login"] == usuario["login"] and login_user["senha"] == usuario["password"]:
            

            entrar_button.config(state= NORMAL)
            remember.new_user(user= login_user)

        else:
            messagebox.showinfo("login incorreto", "Por favor, digite um login e uma senha valida")
            


    def register(event=None):
        if senha_entry.get() == "Digite sua senha" or login_entry.get() == "Digite seu login" or name_entry.get() == "Digite seu nome":
            messagebox.showinfo("Digite um login", "digite um login e uma senha para poder prossegir")
            return

        if senha_entry.get() == "" or login_entry.get() == "" or name_entry.get() == "":
            messagebox.showinfo("Digite um login", "digite um login e uma senha para poder prossegir")
            return

        register = Register(user = {"name": name_entry.get(), "login": login_entry.get(), "password": senha_entry.get()})

        add_user = register.execute()

        if add_user == False:
            messagebox.showinfo("Usuario existe", "O usuario ja existe")
            


    name_entry = Entry_(screen, "Digite seu nome")
    name_entry.pack(pady=(30, 0))
    name_label = Label(screen, text="O nome deve conter no minimo 5 caracteres", font=("Arial", 8))
    name_label.pack()

    login_entry = Entry_(screen, "Digite seu login")
    login_entry.pack(pady=(30, 0))
    login_label = Label(screen, text="O login deve ser unico", font=("Arial", 8))
    login_label.pack()

    senha_entry = Entry_(screen, "Digite sua senha")
    senha_entry.pack(pady=30)


    entrar_button = Button(screen, text="entrar", command= lambda: (screen.state("withdrawn"), chat_screen(), login), state=DISABLED) # Alterar o nome mais tarde
    entrar_button.pack()


    register_button = Button(screen, text="Registrar", command=register)
    register_button.pack()

    login_button = Button(screen, text="Login", command=login)
    login_button.pack()

    remember = RememberMe(user= None)
    if remember.is_user():
        print(remember.data())
        dados = remember.data()
        if not dados == False:
            login_entry.text(dados[1])
            senha_entry.text(dados[2])

    mainloop()

chat_screen()
