''' importações '''
import sqlite3
from supabase import create_client, Client
from os import getenv, path

class Connection:
    def __init__(self):
        URL = "https://tnmhbbojcyptntcznvcy.supabase.co"
        KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRubWhiYm9qY3lwdG50Y3pudmN5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNDM5MzQ3MCwiZXhwIjoyMDQ5OTY5NDcwfQ.ocy4TIpRtT9kNu-sGRdojT7j0jvGasdLSpM1sREgXtA"
        self.supabase: Client = create_client(URL, KEY)

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
        
    def new_user(self, user):
        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT OR REPLACE INTO user 
        (id, nome, login, senha)
        VALUES (?, ?, ?, ?)
        """, (user["id"], user["nome"], user["login"], user["senha"],))

        self.conn.commit()

    def show_name(self):
        cursor = self.conn.cursor()

        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT nome FROM user
        """)

        return cursor.fetchall()
    

        


