from supabase import create_client
from time import localtime
import json
from os import system

def hora():
    return {"mes": localtime().tm_mon, "dia": localtime().tm_mday, "hora": localtime().tm_hour, "minuto": localtime().tm_min}

url = "https://yurkilcutxjmzhbiojkf.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl1cmtpbGN1dHhqbXpoYmlvamtmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzgwNjM0OSwiZXhwIjoyMDQzMzgyMzQ5fQ.MqPS9cCgjrCYZACY9zQZuQsBPV98ZZCo6488Sh_wZgk"

supabase = create_client(url, key)


nome: str = str(input("Digite seu nome: "))

while True:

    hora_atual = hora()
    response = supabase.table('Mensagens').select('*').execute()
    for _ in response.data:
        data = json.loads(_["data"])
        if localtime().tm_mday != hora_atual["dia"]:
            print(f'{data["mes"]}/{data["dia"]} {data["hora"]}:{data["minuto"]}-{_["nome"]} -{_["msg"]}')
        else:
            print(f'{data["hora"]}:{data["minuto"]} {_["nome"]} -{_["msg"]}')



    msg = str(input("Digite uma mensagem: "))
    system("cls")

    data = {
        "data": hora_atual, 
        "nome": nome, 
        "msg": msg}
        
    if msg == "a":
        pass
    else:
        data_add = supabase.table('Mensagens').insert(data).execute()





