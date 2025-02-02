''' importações '''
import sqlite3
from supabase import create_client, Client
from os import getenv, path

class Connection:
    def __init__(self):
        URL = "https://tnmhbbojcyptntcznvcy.supabase.co"
        KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRubWhiYm9qY3lwdG50Y3pudmN5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNDM5MzQ3MCwiZXhwIjoyMDQ5OTY5NDcwfQ.ocy4TIpRtT9kNu-sGRdojT7j0jvGasdLSpM1sREgXtA"
        self.supabase: Client = create_client(URL, KEY)
        
    def show_all_messages(self):
        messages = self.supabase.table('Mensagens').select("*").execute()
        return messages.data
    
    def send_message(self, message):
        self.supabase.table('Mensagens').insert({"nome": message['nome'], "mensagem": message['mensagem']}).execute()
        

class Login(Connection):
    
    def __init__(self, user: dict):
        super().__init__()
        self.user = user

    def execute(self):
        resposta = self.supabase.table('Usuarios').select("*").eq("login", self.user["login"]).execute() # Retorna True se achar o usuario
        print(resposta.data)

        if resposta.data:
            return resposta.data[0]

        return False

class Register(Connection):
    def __init__(self, user: dict):
        super().__init__()
        self.user = user

    def execute(self):
        if_user = self.supabase.table('Usuarios').select("login").eq("login", self.user["login"]).execute()
        print(if_user)
        if not if_user.data:
            usuario = {
                "nome": self.user["name"], 
                "login": self.user["login"], 
                "senha": self.user["password"]
            }

            self.supabase.table('Usuarios').insert(usuario).execute()
            return

        return False


class RememberMe:
    def __init__(self, user):
        self.conn = sqlite3.connect(path.join(getenv("APPDATA") or "", "python_chat.db"))
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        login TEXT,
        senha TEXT
        )
        """)

        self.conn.commit()
        
        cursor.execute("""
        INSERT INTO user (nome, login, senha)
        VALUES (?, ?, ?)
        """, ("", "", ""))
        
        self.conn.commit()
        
    def new_user(self, user):
        cursor = self.conn.cursor()

        cursor.execute("""
        REPLACE INTO user 
        (id, nome, login, senha)
        VALUES (?, ?, ?, ?)
        """, (1, user["nome"], user["login"], user["senha"],))

        self.conn.commit()

    def show_name(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT nome FROM user ORDER BY id LIMIT 1
        """)

        return cursor.fetchone()

    def data(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT nome, login, senha FROM user ORDER BY id LIMIT 1
        """)
        
        result = cursor.fetchone()
        
        if result == ('', '', ''):
            return False

        return result
        
    
    def is_user(self):
        cursor = self.conn.cursor()
        
        cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table';
                       """)
            
        return cursor.fetchone()
    

        


