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
        
        self.geometry("300x300")
        self.login_button = tk.Button(self, text="logar", command=self.login).pack()   
    
    def login(self):
        self.state("withdraw")
        main = Main()
        main.mainloop()
        
if __name__ == "__main__":
    login = Login()
    login.mainloop()
