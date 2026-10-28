import json
import os

ARQUIVO = "funcionarios.json"


def carregar_funcionarios():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_funcionarios(funcionarios):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)


def mostrar_unidades():
    print("1 - Freddy Fazbear's Mega Pizzaplex")
    print("2 - Edwin Murray Costume Manor")
    print("3 - Freddy Fazbear's Pizza")
    print("4 - Fredbear's Family Diner")


def escolher_unidade():
    mostrar_unidades()
    unidade = input("Escolha a unidade: ")

    match unidade:
        case "1":
            return "Freddy Fazbear's Mega Pizzaplex"
        case "2":
            return "Edwin Murray Costume Manor"
        case "3":
            return "Freddy Fazbear's Pizza"
        case "4":
            return "Fredbear's Family Diner"
        case _:
            print("Unidade inválida!")
            return None


def buscar_funcionario(funcionarios, codigo):
    for funcionario in funcionarios:
        if funcionario["codigo"] == codigo:
            return funcionario
    return None


def mostrar_cabecalho():
    print("------ LISTAGEM DE FUNCIONÁRIOS (FAZBEAR ENTERTAINMENT) ------\n")
    print(f"{'CÓDIGO':8} | {'NOME':20} | {'UNIDADE':35} | {'CARGO':20} | {'SALÁRIO':10}")
    print(105 * "-")


def mostrar_funcionario(funcionario):
    print(
        f"{funcionario['codigo']:8} | {funcionario['nome']:20} | {funcionario['unidade']:35} | {funcionario['cargo']:20} | {funcionario['salario']:10.2f}"
    )


def listar_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return None

    mostrar_cabecalho()
    for funcionario in funcionarios:
        mostrar_funcionario(funcionario)
    print("-" * 105)

def cadastrar_funcionario(funcionarios):
    codigo = input("Código do funcionário: ")

    if buscar_funcionario(funcionarios, codigo):
        print("Esse código já está cadastrado!")
        return None

    nome = input("Nome: ")
    unidade = escolher_unidade()

    if unidade is None:
        return None

    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    status = input("Status (Ativo/Inativo): ")

    funcionario = {
        "codigo": codigo,
        "nome": nome,
        "unidade": unidade,
        "cargo": cargo,
        "salario": salario,
        "status": status
    }

    funcionarios.append(funcionario)
    salvar_funcionarios(funcionarios)
    print("Funcionário cadastrado com sucesso!")


def listar_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
   
    mostrar_cabecalho()
    for funcionario in funcionarios:
        mostrar_funcionario(funcionario)
    print("-" * 105)


def consultar_funcionario(funcionarios):
    codigo = input("Digite o código do funcionário: ")
    funcionario = buscar_funcionario(funcionarios, codigo)

    if funcionario:
        mostrar_funcionario(funcionario)
    else:
        print("Funcionário não encontrado.")


def editar_funcionario(funcionarios):
    codigo = input("Digite o código do funcionário: ")
    funcionario = buscar_funcionario(funcionarios, codigo)

    if funcionario is None:
        print("Funcionário não encontrado.")
        return None

    print("Digite os novos dados:")

    nome = input("Nome: ")
    unidade = escolher_unidade()

    if unidade is None:
        return None

    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    status = input("Status (Ativo/Inativo): ")

    funcionario["nome"] = nome
    funcionario["unidade"] = unidade
    funcionario["cargo"] = cargo
    funcionario["salario"] = salario
    funcionario["status"] = status

    salvar_funcionarios(funcionarios)
    print("Funcionário atualizado!")


def excluir_funcionario(funcionarios):
    codigo = input("Digite o código do funcionário: ")
    funcionario = buscar_funcionario(funcionarios, codigo)

    if funcionario is None:
        print("Funcionário não encontrado.")
        return None

    funcionarios.remove(funcionario)
    salvar_funcionarios(funcionarios)
    print("Funcionário excluído!")


def mostrar_menu():
    print("\n=== FAZBEAR HELPER ===")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Consultar funcionário")
    print("4 - Editar funcionário")
    print("5 - Excluir funcionário")
    print("0 - Sair")


def executar_opcao(opcao, funcionarios):
    match opcao:
        case "1":
            cadastrar_funcionario(funcionarios)
        case "2":
            listar_funcionarios(funcionarios)
        case "3":
            consultar_funcionario(funcionarios)
        case "4":
            editar_funcionario(funcionarios)
        case "5":
            excluir_funcionario(funcionarios)
        case "0":
            pass
        case _:
            print("Opção inválida!")


def menu():
    funcionarios = carregar_funcionarios()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "0":
                salvar_funcionarios(funcionarios)
                print("Saindo do Fazbear Helper...")
                break
            case _:
                executar_opcao(opcao, funcionarios)


menu()