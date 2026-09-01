import os
os.system("cls")

# modos de aberturas:w, r, a, (x), (+), with
# x - gravação de arquivo
with open("dados.txt", "w+", encoding="utf-8") as arq:
    arq.write("Linha gravada1\n")
    arq.write("Linha gravada2\n")
    arq.write("Linha gravada3\n")
    arq.write("Linha gravada4\n")    
    arq.seek(0) # movimenta o cursor no arquivo texto
    #print(arq.read())
    print(arq.readline()) #captura do cursor até o final da linha
    arq.seek(20)
    linhas = arq.readlines() # cria uma lista e joga cada linha em um elemento
    print(linhas)
    print(linhas[2], len(linhas[2]))
    # "Linha gravada 3"
    x = linhas[2].split()
    print(x)
    # x = ["Linha", "gravada", "3"]
    texto = "".join(x)
    # "Linhagravada"
    print(texto)
    arq.write(texto)

    with open("cidades.txt", "w", encoding="utf-8") as arq:
        cidades = ("São Paulo", "Rio de Janeiro", "Recife")
        arq.writelines(cidades)

def grava_linhas_arquivo(na: str, l: list) -> None:
     with open(na, "w", encoding="utf-8") as arq:
        arq.writelines(l)
        print("Arquivo '{na}' gravado com sucesso!")

# principal
nome_arquivo = "cidades.txt"
cidades = ("São Paulo\n", "Goias\n", "Rio de Janeiro\n", "Recife\n")
grava_linhas_arquivo(nome_arquivo, cidades)

