import os
os.system("cls")

arquivo = "Teste.txt"

while True:
    print("""----------------------------
0 - Sair
1 - Exibir conteúdo
2 - Adicionar texto
3 - Contar palavras
4 - Contar caracteres
5 - Procurar palavra
6 - Contar palavras com N letras
7 - Mostrar linha específica
8 - Excluir txt
----------------------------
""")
    escolha = int(input("Escolha uma opção: "))

    match escolha:
        
        case 0:
            with open(arquivo, "w") as arq:
                print("Obrigado por usar meu código!")
                break
        
        case 1:
            with open(arquivo, "r") as arq:
                print(arq.read())
                arq.close
        
        case 2:
            linha = str(input("Digite seu texto: "))
            with open(arquivo, "a", encoding= "utf-8") as arq:
                arq.write(linha + "\n")
                print("Linha adicionada!")
                arq.close()
        
        case 3:
            total_palavras = 0
            with open(arquivo, "r", encoding= "utf-8") as arq:
                for linha in arq:
                    total_palavras += len(linha.split(" "))
                print(f"Seu arquivo tem {total_palavras} palavras")

        case 4:
            total_caracteres = 0
            with open(arquivo, "r", encoding= "utf-8") as arq:
                conteudo = arq.read()
                total_caracteres = len(conteudo) - 1
                print(f"Seu arquivo tem {total_caracteres} caracteres")

        case 5:
            proc_palavra = str(input("Digite a palavra que deseja procurar: "))
            vezes = 0

            if proc_palavra == "1234567890":

                print("Digite apenas palavras!!")

            else:
                with open(arquivo, "r", encoding="utf-8") as arq:
                    conteudo = arq.readlines()
                    conteudo = "".join(conteudo)
            for palavra in conteudo.split():
                if palavra == proc_palavra:
                    vezes += 1
            print(f"Sua palavra aparece {vezes} vezes")
        
        case 6:
            qtd_palavra = int(input("Digite a quantidade de letras: "))

            cont = 0

            with open(arquivo, "r", encoding="utf-8") as arq:
                for linha in arq:
                    xpalavras = linha.split()
                    for palavra in xpalavras:
                        if len(palavra) == qtd_palavra:
                            cont += 1

            print(f"Quantidade de palavras com {qtd_palavra} letras: {cont}")

        case 7:
            linha_esp = int(input(("Digite a linha que você gostaria de ver: ")))
            linha = []
            with open(arquivo, "r") as arq:
                linha = arq.readlines()
                print(linha[linha_esp-1])

        case 8:
            import os
            os.system("del Teste.txt")

        case _:
            print("Digite uma opção válida!")

            
