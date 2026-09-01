#dado um numero pelo usuario exibir os 10 primeros multiplos. 
# Perguntar ao usuario se ele quer gravar na mesma linha ou em linha separada.
#o nome do arquivo texto Prova.txt .
#Toda vez que pedir um numero, apagar o conteudo do arquivo antes de gravar

import os
os.system("cls")

arquivo = "Prova.txt"

while True:
    print ("""
    ~~~~~~~~~Menu~~~~~~~~~~~~
       0 - Sair
       1 - Multiplos
       2 - Exibir conteudo do arq
    ~~~~~~~~~~~~~~~~~~~~~~~~
    """)   
    escolha = int(input("Digite sua escolha: "))
    match escolha:
        case 0:
            print("Obrigado por usar nosso código!")
            break

        case 1:
            print ("""
     ~~~~~ESCOLHA~~~~~~
     De que forma exbir:
     1 - Por linha
     2 - Uma só linha
     ~~~~~~~~~~~~~~~~~~
                    """
            )
            escolha2 = int(input("Digite a opção: "))

            multiplo = int(input("Digite um número: "))
            match escolha2:
                case 1:
                    with open (arquivo, "w", encoding="utf-8") as arq:
                        for i in range(1, 11, 1):
                            multi = multiplo * i
                            resul = (f"{multi}\n")
                            arq.write(resul)
                        print ("Adicianado ao Arquivo!!") 
                        arq.close()
                        continue
                case 2:
                    with open (arquivo, "w", encoding="utf-8") as arq:
                        for i in range(1, 11, 1):
                            multi = multiplo * i
                            resul2 = (f"{multi} " " ")
                            arq.write(resul2)
                        print ("Adicianado ao Arquivo!!") 
                        arq.close()
                        continue
                case _:
                    print ("ERRO! Digite uma opção valida!!")
                    continue    
                     

        case 2:
            with open(arquivo, "r") as arq:
                conteudo = arq.read()
                print(conteudo)
            arq.close()        
            continue

        case _:
            print ("ERRO! Digite uma opção valida!!")
            continue
             