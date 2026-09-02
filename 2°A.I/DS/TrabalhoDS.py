import os
os.system("cls")


dict = {}
while True:
    print("""
        M E N U
        -------
        0 - Sair
        1 - Zerar o dicionario
        2 - Adicionar uma key
        3 - Editar um value
        4 - Remover uma key
        5 - Exibe o dicionário\n
""")
    
    escolha = int(input("Escolha:  "))
    match escolha:
        case 0:
            print("Obrigado por usar nosso código!")
            break
        case 1:
            dict = {}
            print (">>>>> Dicionario zerado!!\n")
            input("Pressione algo para continuar...")

        case 2:
            newkey = input ("Nome da key: ")
            if newkey in dict:
                print(f">>>>> A key '{newkey}' já existe!\n")
                input("Pressione algo para continuar...")
            
            elif newkey == None:
                print("ERRO! Nenhuma key digitada, tente novamente\n")
                input("Pressione algo para continuar...")

            else:
                print("""
    1 - int
    2 - float
    3 - str
    4 - bool\n
                """)
                escolha2 = str(input("Selecione: "))
                conteudo = str(input("Conteudo: "))
                match escolha2:
                    case '1' | 'int':
                        
                        try:
                            conteudo = 0 if conteudo == "" else int(conteudo)
                        except ValueError:
                            print("Valor de categoria errada!")
                            continue
                    case '2' | 'float':
                        try:
                            conteudo = 0.0 if conteudo == "" else float(conteudo)
                        except ValueError:
                            print("Valor de categoria errada!")
                            continue
                    case '3' | 'str':
                        try:
                            conteudo = "" if conteudo == "" else conteudo
                        except ValueError:
                            print("Valor de categoria errada!")
                            continue
                    case '4' | 'bool':
                        try:
                            conteudo = False if conteudo == "" else bool(conteudo)
                        except ValueError:
                            print("Valor de categoria errada!")
                            continue
                dict[newkey] = conteudo 
                print (f"'{newkey}: {conteudo}' criado com sucesso!\n")
                input("Pressione algo para continuar...")
       
        case 3:
            if dict == None:
                print("Dicionário vazio!")
                continue
            else:
                num = 0
                tamanho_total = 13
                print("Keys:")
                for k, v in dict.items():
                    num += 1
                    print(f"{num} - {k}: {v}")
                escolha3 = int(input("Número da chave: "))

                if escolha3 == num:
                    mod_value = input("Novo valor: ")
                    v = mod_value
                    dict[k] = mod_value
                print("----- Conteúdo do dicionário")
                for k,v in dict.items():
                    qtd_pontos = tamanho_total - len(k)
                    pontos = "." * qtd_pontos
                    print(f"{k}{pontos}: {v}")                    
                print("-" * 28)
                