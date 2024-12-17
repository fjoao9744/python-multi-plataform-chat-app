''' importações '''
from supabase import create_client, Client

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
        resposta = self.supabase.table('Usuarios').select("login").eq("login", self.user["login"]).execute() # Retorna True se achar o usuario

        if resposta.data:
            return True

        return False

class Register(Connection):
    def __init__(self, user: dict):
        super().__init__()
        self.user = user

