from tkinter import *

# Configurações da tela
screen = Tk()
screen.geometry("350x400")
screen.config(bg="#2B2B33")
screen.title("Chat Online")


                                                            # Aba de inserção do nome

def name_save(event=None): # Salva o nome na entrada

    #formatação do nome para evitar erros
    name = name_entry.get().strip()
    name = ' '.join(name.capitalize().split())
    
    if len(name) < 4 or len(name) > 12:
        len_warning.pack()

    else:
        # Adiciona o nome ja formatado
        name_entry.delete(0, END)
        name_entry.insert(0, name)

        len_warning.pack_forget()
        name_save_button["state"] = DISABLED
        name_edit_button["state"] = NORMAL
        name_entry.config(state='disabled')

    
def name_edit(event=None): # Reaciona a entrada e o botão de salvar
        name_save_button["state"] = NORMAL
        name_edit_button["state"] = DISABLED
        name_entry.config(state='normal')

name_frame = Frame(bg="#2B2B33") # O frame onde vai ficar os widgets principais

# Widgets principais
name_save_button = Button(name_frame, text="save", bg="#2D2B41", relief=SOLID, fg='#C2CDE9', font=("Courier", 12), command=name_save)
name_edit_button = Button(name_frame, text="edit", bg="#2D2B41", relief=SOLID, fg='#C2CDE9', font=("Courier", 12), command=name_edit, state="disabled")
name_entry = Entry(name_frame, bg="#39366B", relief=SOLID, bd=2, fg='#C2CDE9', font=("Courier", 12))
name_entry.bind("<Return>", name_save)

# Aviso caso exceda o limite de caracteres
len_warning = Label(screen, text="O nome deve conter de 4 a 12 caracteres.", bg="#2B2B33", fg="red")


# Metodos geométricos
name_frame.pack()
name_entry.pack(padx=(10, 0), pady=5, anchor=N, side=LEFT, ipady=3)
name_save_button.pack(padx=(10, 5), pady=4, anchor=N, side=LEFT)
name_edit_button.pack(padx=5, pady=4, anchor=N, side=LEFT)

len_warning.pack_forget()

mainloop()