import tkinter as tk
from methods import MessageList, Send

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.state("zoomed")
        Mlist = MessageList(self)
        Mlist.size(40, 150)
        
        Sinput = Send.Input(self)
        Sbutton = Send.Button(self)
        Sbutton.input_define(Sinput)

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x400")
        
        # entrys
        self.nome_label = tk.Label(self, text="digite seu nome", font=("Arial", 15)).pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()
        
        self.login_label = tk.Label(self, text="digite um login", font=("Arial", 15)).pack()
        self.login_entry = tk.Entry(self)
        self.login_entry.pack()
        self.login_labelFoot = tk.Label(self, text="algo para poder logar novamente mais tarde", font=("Arial", 9)).pack()
        
        self.password_label = tk.Label(self, text="digite uma senha", font=("Arial", 15)).pack()
        self.password_entry = tk.Entry(self)
        self.password_entry.pack()
        self.password_labelFoot = tk.Label(self, text="evite usar uma senha pessoal ou que ja tenha usado", font=("Arial", 9)).pack()
        
        
        
        self.login_label = tk.Label(self, text="algo para poder logar novamente mais tarde")
        
        self.login_button = tk.Button(self, text="logar", command=self.login).pack()
        
    
    def login(self):
        self.state("withdraw")
        main = Main()
        main.mainloop()
        

if __name__ == "__main__":
    login = Login()
    login.mainloop()
