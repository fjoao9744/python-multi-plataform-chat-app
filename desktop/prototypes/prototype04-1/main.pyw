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

main = Main()
main.mainloop()