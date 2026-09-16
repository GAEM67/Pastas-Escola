import os
os.system("cls")
# SUBALGORITMOS
os.system("cls")
def exibe_dados(p: dict) -> None:
    for k1, v1 in p.items():
        print(f"Nome: {k1}")
        for k2, v2 in v1.items():
            if isinstance(v2, dict): # se for um dicionario
                # tratar como dicionario - Particionar as informacoes
                print(f"\t{k2}")
                for k3, v3 in v2.items():
                    print(f"\t\t{k3}: {v3}")
            else:
                # tratar como um outro dado (simples)
                print(f"\t{k2}: {v2}")

def key_existe(p: dict, k: str) -> bool:
    return k in p

def cad_pessoa(p: dict,c: str, k: str, u: str) -> dict:
    if key_existe(p, u): # se existir
        k = input("Nova chave: ")
        c = input("Conteudo: ")
        p[u][k] = c
    else:
        print("Pessoa nao existe!")    
    return pessoa2

def nom_irma(k: str, nm: str, p: dict,n: int) -> dict:
    while True:
        nm = input("Nome irmão: ")
        if nm != "":
            n = len(p["Edson"]["irmaos"]) + 1
            k = f"irmao{n}"
            p["Edson"]["irmaos"][k] = nm
        else:
            break
        return pessoa2


# Dicionário de dicionário (níveis)
pessoa = {
    "Edson":{
        "nomepai": "Jurandir",
        "nomemae": "Ester",
        "irmao": "Edilson",
    },
    "Marcelo":{
        "nomepai": "Antonio",
        "nomemae": "Maria",
        "irmao": "Adriano",
    }
}

pessoa2 = {
    "Edson":{
        "nomepai": "Jurandir",
        "nomemae": "Ester",
        "irmaos": {
            "irmao1":"Edilson",
            "irmao2":"Elaine",
        }
    },
    "Marcelo":{
        "nomepai": "Antonio",
        "nomemae": "Maria",
        "irmaos": {
            "irmao1": "Adriano",
            "irmao2": "Samuel",
            "irmao3": "Carla",
        }
    }
}


# Exibir o dicionario de forma correta
os.system("cls")
exibe_dados(pessoa2)

# Criando uma key nivel 1
nome_irmao = ""
numero = 0
conteudo = ""
chave = ""
usuario = input("Pessoa: ")
cad_pessoa(pessoa2, conteudo, chave, usuario)

exibe_dados(pessoa2)



nom_irma(chave,nome_irmao,pessoa2,numero)

exibe_dados(pessoa2)





