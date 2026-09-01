import os

try:
    os.system("clear")
except:
    pass


def inicializar_estoque():
    estoque = {}

    try:
        quantidade = int(input("Digite a quantidade de produtos diferentes: "))
    except ValueError:
        print("Digite um número válido.")
        return estoque

    for i in range(quantidade):
        produto = input(f"Digite o nome do produto {i + 1}: ")
        qtd = input(f"Digite a quantidade do produto {i + 1}: ")
        estoque[produto] = qtd

    return estoque


def modificar_quantidade(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    produto = input("Digite o nome do produto que deseja modificar a quantidade: ")

    if produto in estoque:
        nova_qtd = input("Digite a nova quantidade: ")
        estoque[produto] = nova_qtd
        print("Quantidade modificada com sucesso.")
    else:
        print("Produto não encontrado.")


def modificar_produto(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    produto_antigo = input("Digite o nome do produto que deseja modificar: ")

    if produto_antigo in estoque:
        novo_produto = input("Digite o novo nome para o produto: ")

        if novo_produto in estoque and novo_produto != produto_antigo:
            print("O novo produto já existe no estoque.")
        else:
            estoque[novo_produto] = estoque.pop(produto_antigo)
            print("Nome do produto modificado com sucesso.")
    else:
        print("Produto não encontrado.")


def remover_produto(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    produto = input("Digite o nome do produto que deseja remover: ")

    if produto in estoque:
        del estoque[produto]
        print("Produto removido com sucesso.")
    else:
        print("Produto não encontrado.")


def listar_produtos(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    print("\n--- Lista de Produtos ---")
    for produto in estoque:
        print(f"- {produto}")


def listar_quantidades(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    print("\n--- Lista de Quantidades ---")
    for qtd in estoque.values():
        print(f"- {qtd}")


def exibir_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return

    print("\n--- Estoque Completo ---")
    for produto, qtd in estoque.items():
        print(f"Produto: {produto} | Quantidade: {qtd}")


estoque = {}

while True:
    print(
        """
===========Menu===========
0 - Sair
1 - Inicializar o estoque
2 - Modificar uma quantidade
3 - Modificar o nome de um produto
4 - Remover um produto
5 - Listar os produtos
6 - Listar as quantidades
7 - Exibir o estoque completo
==========================
"""
    )
    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Digite uma opção válida (número inteiro).")
        continue

    if opcao == 0:
        print("Programa encerrado.")
        break

    elif opcao == 1:
        estoque = inicializar_estoque()
        print("Estoque inicializado com sucesso.")

    elif opcao == 2:
        modificar_quantidade(estoque)

    elif opcao == 3:
        modificar_produto(estoque)

    elif opcao == 4:
        remover_produto(estoque)

    elif opcao == 5:
        listar_produtos(estoque)

    elif opcao == 6:
        listar_quantidades(estoque)

    elif opcao == 7:
        exibir_estoque(estoque)

    else:
        print("Opção inválida.")