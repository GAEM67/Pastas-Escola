import os
os.system("cls")

def gravar_arquivo(na: str) -> None:
    with open(na, "a", encoding="utf-8") as arquivo:
        print("Digite o nome ou ENTER em nome para finalizar...")
        while True:
            print(30 * '-')
            nome = input("Nome: ")
            if nome == '':
                break
            else:
                idade = int(input("Idade: "))
                altura = float(input("Altura: "))
                arquivo.write(f"{nome},{idade},{altura}\n")

def listar_arquivo(na: str) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista = linha.split(',')
            print(30 * '-')
            print(f"Nome.........: {lista[0]}")
            print(f"Idade........: {lista[1]}")
            print(f"Altura.......: {lista[2]}")

def exibir_linha(l: list) -> None:
    print("Registro:" + 30 * '-' )
    print(f"Nome.........: {l[0]}")
    print(f"Idade........: {l[1]}")
    print(f"Altura.......: {l[2]}")
    print(30 * '-')

def pesquisar_nome(na: str, n: str) -> bool:
    encontrou = False
    with open(na, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista = linha.split(',')
            if lista[0] == n:
                exibir_linha(lista)
                encontrou = True
    return encontrou

def pesquisar_idade(na: str) -> None:
    print("""
---------- S U B - M E N U (IDADE) ----------
    1 - Simples
    2 - Maior ou igual
    3 - Menor ou igual
    4 - Entre
---------------------------------------------
""")
    sub_escolha = input("Escolha: ")
    encontrou = False
    
    with open(na, "r", encoding="utf-8") as arquivo:
        if sub_escolha == '1':
            idade_busca = int(input("Idade -> Pesquisar: "))
            for linha in arquivo:
                lista = linha.split(',')
                if int(lista[1]) == idade_busca:
                    exibir_linha(lista)
                    encontrou = True
                    
        elif sub_escolha == '2':
            idade_busca = int(input("Idade maior ou igual a: "))
            for linha in arquivo:
                lista = linha.split(',')
                if int(lista[1]) >= idade_busca:
                    exibir_linha(lista)
                    encontrou = True
                    
        elif sub_escolha == '3':
            idade_busca = int(input("Idade menor ou igual a: "))
            for linha in arquivo:
                lista = linha.split(',')
                if int(lista[1]) <= idade_busca:
                    exibir_linha(lista)
                    encontrou = True
                    
        elif sub_escolha == '4':
            inicio = int(input("inicio: "))
            fim = int(input("fim: "))
            for linha in arquivo:
                lista = linha.split(',')
                if inicio <= int(lista[1]) <= fim:
                    exibir_linha(lista)
                    encontrou = True
                    
    if not encontrou:
        print("Nenhum registro encontrado para esta idade.")

def pesquisar_altura(na: str) -> None:
    print("""
---------- S U B - M E N U (ALTURA) ----------
    1 - Simples
    2 - Maior ou igual
    3 - Menor ou igual
    4 - Entre
---------------------------------------------
""")
    sub_escolha = input("Escolha: ")
    encontrou = False
    
    with open(na, "r", encoding="utf-8") as arquivo:
        if sub_escolha == '1':
            altura_busca = float(input("Altura -> Pesquisar: "))
            for linha in arquivo:
                lista = linha.split(',')
                if float(lista[2]) == altura_busca:
                    exibir_linha(lista)
                    encontrou = True
                    
        elif sub_escolha == '2':
            altura_busca = float(input("Altura maior ou igual a: "))
            for linha in arquivo:
                lista = linha.split(',')
                if float(lista[2]) >= altura_busca:
                    exibir_linha(lista)
                    encontrou = True
                    
        elif sub_escolha == '3':
            altura_busca = float(input("Altura menor ou igual a: "))
            for linha in arquivo:
                lista = linha.split(',')
                if float(lista[2]) <= altura_busca:
                    exibir_linha(lista)
                    encontrou = True
                    
        elif sub_escolha == '4':
            inicio = float(input("inicio: "))
            fim = float(input("fim: "))
            for linha in arquivo:
                lista = linha.split(',')
                if inicio <= float(lista[2]) <= fim:
                    exibir_linha(lista)
                    encontrou = True
                    
    if not encontrou:
        print("Nenhum registro encontrado para esta altura.")

nome_arquivo = "arquivo.txt"

while True:
    os.system('cls')
    print(""" 
---------- M E N U ----------
      0 - Sair
      1 - Gravar linhas
      2 - Listar arquivo
      3 - Pesquisar 
--------------------------------
          """)
    escolha = int(input("Escolha: "))

    match escolha:
        case 0:
            print("Obrigado por usar o código!")
            break

        case 1:
            gravar_arquivo(nome_arquivo)

        case 2:
            listar_arquivo(nome_arquivo)
            input("\nPressione ENTER para continuar...")

        case 3:
            print("""
---------- S U B M E N U ----------
      1 - Nome 
      2 - Idade
      3 - Altura
----------------------------------
""")
            escolha2 = int(input("Escolha: "))

            match escolha2:
                case 1:
                    nome_procurado = input("Nome: ")
                    if not pesquisar_nome(nome_arquivo, nome_procurado):
                        print(f"O nome '{nome_procurado}' não existe no arquivo")
                case 2:
                    pesquisar_idade(nome_arquivo)
                case 3:
                    pesquisar_altura(nome_arquivo)
                case _:
                    print("Opção inválida!")
            
            input("\nPressione ENTER para continuar...")

        case _:
            print("Erro! Digite uma opção valida!")
            input("\nPressione ENTER para continuar...")