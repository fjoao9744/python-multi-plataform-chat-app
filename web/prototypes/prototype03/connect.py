from supabase import create_client, Client

url = "https://yurkilcutxjmzhbiojkf.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl1cmtpbGN1dHhqbXpoYmlvamtmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzgwNjM0OSwiZXhwIjoyMDQzMzgyMzQ5fQ.MqPS9cCgjrCYZACY9zQZuQsBPV98ZZCo6488Sh_wZgk"

supabase: Client = create_client(url, key)

# Vai carregar todas as mensagens
messages = supabase.table('Mensagens').select("*").order('id', desc=True).execute()

def send_message(name, message):
    def hora_atual():
        from time import localtime

        return {"mes": localtime().tm_mon, "dia": localtime().tm_mday, "hora": localtime().tm_hour, "minuto": localtime().tm_min}

    message = {"data" : hora_atual(), "nome" : name, "msg" : message}
    supabase.table('Mensagens').insert(message).execute()
