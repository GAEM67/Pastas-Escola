import os

os.system("cls")
# Erick Martins e Gustavo Andrews

from Funcoes import*

# --- Programa Principal ---
dict_ = {}

while True:
    menu()

    try:
        escolha1 = int(input("Escolha:  "))
    except ValueError:
        print("Por favor, insira um número válido do menu.")
        input("Pressione algo para continuar...")
        continue

    match escolha1:
        case 0:
            print("Obrigado por usar nosso código!")
            break

        case 1:
            dict_ = {}
            print(">>>>> Dicionario zerado!!\n")
            input("Pressione algo para continuar...")

        case 2:
            newkey = obter_novo_key_nome(dict_)
            if newkey is not None:
                obter_conteudo_validado(dict_, newkey)
                input("Pressione algo para continuar...")

        case 3:
            if dict_vazio(dict_):
                continue

            key_sel = select_key(dict_)
            if key_sel is not None:
                obter_conteudo_validado(dict_, key_sel)
                exibir_dict(dict_)
                input("Pressione algo para continuar...")

        case 4:
            if dict_vazio(dict_):
                continue

            key_sel = select_key(dict_)
            if key_sel is not None:
                del dict_[key_sel]
                if not dict_:
                    print(">>>>> Dicionário esvaziado!")
                else:
                    exibir_dict(dict_)
                input("Pressione algo para continuar...")

        case 5:
            exibir_dict(dict_)
            input("Pressione algo para continuar...")

        case _:
            print("Opção de menu inválida!")
            input("Pressione algo para continuar...")