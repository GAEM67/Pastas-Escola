import os
import time
os.system('cls')

"""
# ARQUIVOS TEXTO
# Modo de abertura | Descrição
#-----------------------------
# "w" = write      | Cria (ou recicla) um arquivo para exibição
# "r" = read       | Lê um arquivo existente

# Sintaxe para abertura de arquivos - open()
# [objeto] = open(nome_arquivo, modo_abertura,...)

arq = open("arq01.txt", "w", encoding="utf-8")
arq.write("Estou testando gravação de arquivos!") # escreve no arquivo
arq.write("\nnova linha") # escreve no arquivo
arq.close()

# Leitura do arquivo
arq = open("arq01.txt", "r", encoding="utf-8")
print(arq.read()) # lê todo o arquivo
arq.close()
"""
# Exercicio: Faça o seguinte menu:
"""
0 - SAIR
1 - Nome do arquivo 
2 - Gravar arquivo
3 - Exibir arquivo

Escolha: _

"""

while True:

    print("=========MENU=========")
    print("0 - SAIR")
    print("1 - Nome do arquivo")
    print("2 - Gravar arquivo")
    print("3 - Exibir arquivo")
    escolha = int(input("Escolha: "))

    if escolha ==0:
        print("Saindo do programa")
        os.system('pause')
        os.system('cls')
        break
    elif escolha == 1:
        nome = input("Nomeie o arquivo: ")
        print("Nomeando arquivo")
        
        arq = open(nome + ".txt", "w", encoding="utf-8")
        arq.close()
        os.system('pause')
        os.system('cls')
    elif escolha == 2:
        mensagem = input("Digite algo que deseja gravar: ")
        print("Gravando mensagem")
        arq = open(nome + ".txt", "w", encoding="utf-8")
        arq.write(mensagem)
        os.system('pause')
        os.system('cls')
    elif escolha == 3:
        print("Abrindo o arquivo")
       
        arq = open(nome + ".txt", "r", encoding="utf-8")
        print(arq.read())
        arq.close()
        os.system('pause')
        os.system('cls')
    else:
        print("Erro!")
        print("Digite uma das opções válidas")
        os.system('pause')
        os.system('cls')
        continue

        