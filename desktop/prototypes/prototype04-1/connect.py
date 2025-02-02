from supabase import create_client, Client

class Connection:
    def __init__(self):
        URL = "https://tnmhbbojcyptntcznvcy.supabase.co"
        KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRubWhiYm9qY3lwdG50Y3pudmN5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNDM5MzQ3MCwiZXhwIjoyMDQ5OTY5NDcwfQ.ocy4TIpRtT9kNu-sGRdojT7j0jvGasdLSpM1sREgXtA"
        self.supabase: Client = create_client(URL, KEY)
        
    def show_all_messages(self):
        messages = self.supabase.table('Mensagens').select("*").execute()
        return messages.data
        
    def send_message(self, message: dict):
        # TODO: ajustar isso mais tarde antes de enviar qualquer coisa
        self.supabase.table('Mensagens').insert(message).execute()
        

            
        
        
        


