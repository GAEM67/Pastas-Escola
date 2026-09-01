#Gustavo Andrews Meirinho Lencina 2°AI
#Erick Martins de Faria 2°AI
#Nao conseguimos apagar o arquivo
import os
os.system("cls")

palavras = 0
while True:

    print("""        ~~~~~~~~~~Menu~~~~~~~~~~~
          0 - Sair
          1 - Gravar linha no arquivo
          2 - Contar palavras com 5 caracteres
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    escolha = int(input("Escolha sua opção: "))
                  
    match escolha:
        case 0:
            print("Obrigado por usar nosso programa!!")
            #Nao conseguimos apagar o arquivo
            break
    
        case 1:
             arq = open ("arq.txt", "a", encoding = "utf-8")
             linha = str(input("Grave sua linha: "))
             arq.write("Conteúdo:\n")
             arq.write(f"{linha}")
             arq.write("\n")
             arq.close()

        case 2:
            with open("arq.txt", "r", encoding="utf-8") as arq:
             v = arq.read()
             f = v.split(" ")

             for r in f:
                 if 5 == len(r):
                     palavras += 1
                     print(f"Sua linha tem {palavras} palavras com 5 caracteres")    
        case _:
            print("Escolha inválida")              
                    
    