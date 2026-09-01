
import os
os.system('cls')

arquivo = "Projeto.txt"
while True:
    print ('''
    --------------------------------------
    0 - Sair
    1 - Gravar linha
    2 - Gravar linhas
    3 - Exibir o conteudo do arquivo
    4 - Exibir uma linha dada pelo usuario
    5 - Contar palavras
    6 - Contar caracteres
    7 - Contar palavras com N letras
    8 - Contar palavras dadas pelo usuário
    ---------------------------------------''')

    escolha = int(input("Escolha: "))

    match escolha: 
        case 0:
            with open(arquivo, "w") as arq:
                ...  
            print("Arquivo limpo. Programa encerrado.")
        
            break

        case 1:
            linha = input("Digite o conteúdo: ")

            with open(arquivo, "a") as arq:
             arq.write(linha + "\n")

            print("Linha gravada com sucesso!")
        
        case 2:
            linhas = []
            print ("Digite suas linha e dê Enter em uma linha vazia para encerrar!!")

           
            while True:
                
                linha2 = input("Digite uma linha: ")
                linhas.append(linha2 +"\n")
                if linha2 == "":
                    break
                with open(arquivo, "w", encoding="utf-8") as arq:
                    arq.writelines(linhas)

                print ("Linha adicionada!")

        case 3:
            arq = open(arquivo, "r", encoding="utf-8")
            print(arq.read())
            arq.close()
            
        case 4:
            veinhas = []
            uslinha = int(input("Escolher a linha que deseja ver: "))
            with open (arquivo, "r", encoding="utf-8") as arq:
                veinhas = arq.readlines()
                print(veinhas[uslinha-1])

        case 5:
             total_palavras = 0
             with open(arquivo, "r", encoding="utf-8") as arq:
                        for linha in arq:
                            total_palavras += len(linha.split(" "))
                            
             print(f"O total de palavras eh: {total_palavras}")

        case 6:
            total_caracteres = 0
            with open(arquivo, "r", encoding="utf-8") as arq:
                conteudo = arq.read()
                total_caracteres = len(conteudo)
                print(f"O total de caracteres eh: {total_caracteres}")
        
        case 7: 

            print ("Contar palavras com um quantia de letras")
            qtd_letras = int(input("Digite a quantidade de letras que você quer: "))

            contador = 0
    
            with open(arquivo, "r") as arq:

                    for linha in arq:
                    
                        xpalavras = linha.split()
                    
                    for palavra in xpalavras:
                        if len(palavra) == qtd_letras:
                            contador += 1

            print(f"Quantidade de palavras com {qtd_letras} letras: {contador}")

        case 8:

            userpalavra = input("Digite a palavra que deseja saber a quantidade: ")
            contador2 = 0
            ypalavras = []
            with open(arquivo, "r") as arq:

              for linha in arq:
                    
                ypalavras = linha.split()
                    
                for palavra in ypalavras:
                  if userpalavra in ypalavras:
                    contador2 += 1 
            
            print(f"Quantidade de palavras({userpalavra}): {contador2}") 

        case _:
            print("Erro! Opção Iválida")



            





            
            

        