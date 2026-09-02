import os

os.system("cls")

def inicializar_dicionario():
     sabor = {}
     quantidade = int(input("Quantas opções você deseja cadastrar: "))
    
     for i in range(quantidade):
        key = input(f"Digite a key {i + 1}: ")
        value = input(f"Digite o value {i + 1}: ")
        sabor[key] = value
     return sabor

def add_key_e_value(sabor):
    add_key = input("Digite uma key: ")
    add_value = input("Digite um value: ")
    sabor[add_key] = add_value
    print("Item adicionado com sucesso!")

def mod_value(sabor):
    if not sabor:
        print("Dicionario vazio!")
        return
    
    key = input("Digite a key do value que deseja modificar: ")
    if key in sabor:
        mod_value = input("Digite o novo value: ")
        sabor[key] = mod_value
        print("Value modificado com sucesso!")
    else:
        print("Key nao encontrada!")

def mod_key(sabor):
    if not sabor:
        print("Dicionario vazio!")
        return
    
    key = input("Digite a key que deseja alterar: ")
    if key in sabor:
        mod_key = input("Digite a nova key: ")
        sabor[mod_key] = sabor.pop(key)
        print("Key modificada com sucesso!")
    else:
        print("Key nao encontrada!")

def remov_value(sabor):
    if not sabor:
        print("Dicionario vazio!") 
        return
    key = input("Digite a key do value que deseja remover: ")
    if key in sabor:
        del sabor[key]
        print("Value removido com sucesso!")
    else:
        print("Key nao encontrada")

def remov_key(sabor):
    if not sabor:
        print("Dicionario vazio!") 
        return
    key = input("Digite a key deseja remover: ")
    if key in sabor:
        del sabor[key]
        print("Key removido com sucesso!")
    else:
        print("Key nao encontrada")

def list_keys(sabor):
    if not sabor:
        print("O dicionario esta vazio.")
        return
    
    print("Keys:")
    for key in sabor:
        print(key)

def list_value(sabor):
    if not sabor:
        print("O dicionario esta vazio.")
        return
    
    print("Values:")
    for value in sabor.values():
         print(value)

def exib_dic(sabor):
     if not sabor:
        print("O dicionario esta vazio.")
        return
     print("Dicionario:")
     print(sabor)

sabor = {}

while True:
    print(
        """
    ===== MENU =====
0 - Sair
1 - Inicializar o dicionário
2 - Adicionar uma key e value
3 - Modificar um value
4 - Modificar uma key
5 - Remover um value
6 - Remover uma key
7 - Listar as keys
8 - Listar os values
9 - Exibir o dicionário
"""
    )
    escolha = int(input("Digite sua opção: "))

    match escolha:
        case 0:
            print("Obrigado por usar nosso código!")
            break

        case 1:
           sabor = inicializar_dicionario()

        case 2:
            add_key_e_value(sabor)

        case 3:
           mod_value(sabor)

        case 4:
           mod_key(sabor)
        case 5:
            remov_value(sabor)

        case 6:
            remov_key(sabor)

        case 7:
           list_keys(sabor)

        case 8:
           list_value(sabor)

        case 9:
           exib_dic(sabor)

        case _:
            print("Opção invalida!")