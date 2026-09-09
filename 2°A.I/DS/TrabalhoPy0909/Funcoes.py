import os
os.system("cls")

def menu() -> None:
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
def escolhavar(escolha2: str, conteudo: str) -> str | float | int | bool | None:
    match escolha2:
        case '1' | 'int':
            try:
                return 0 if conteudo == "" else int(conteudo)
            except ValueError:
                return None

        case '2' | 'float':
            try:
                return 0.0 if conteudo == "" else float(conteudo)
            except ValueError:
                return None

        case '3' | 'str':
            return conteudo

        case '4' | 'bool':
            if conteudo == "" or conteudo.lower() in ("false", "0"):
                return False
            return True

        case _:
            return None

def dict_vazio(dict_: dict) -> bool:
    """Verifica se o dicionário está vazio com aviso ao usuário."""
    if not dict_:
        print("Dicionário vazio!")
        input("Pressione algo para continuar...")
        return True
    return False
def select_key(dict_: dict) -> str | None:
    """Exibe as chaves numeradas usando contador simples no for."""
    print("Keys:")
    chaves = list(dict_.keys())

    # Substituição do enumerate por contador manual
    idx = 1
    for k in dict_:
        print(f"{idx} - {k}: {dict_[k]}")
        idx += 1

    while True:
        try:
            escolha3 = int(input("Número da chave: "))
            if 1 <= escolha3 <= len(chaves):
                return chaves[escolha3 - 1]
            print(f">>>>> '{escolha3}' é um número de chave inválido!")
        except ValueError:
            print(">>>> Entrada inválida! Digite apenas o número da chave.")

        input("Pressione algo para tentar novamente...\n")
        return None
def obter_conteudo_validado(dict_: dict, newkey: str) -> None:
    """Solicita o tipo e o conteúdo, validando até o usuário acertar os dados."""
    print("""
    1 - int
    2 - float
    3 - str
    4 - bool\n
    """)
    while True:
        escolha2 = input("Selecione: ").strip()
        if escolha2 in ('1', '2', '3', '4', 'int', 'float', 'str', 'bool'):
            break
        print("Opção inválida! Escolha entre 1 e 4.")

    while True:
        conteudo = str(input("Conteudo: "))
        resultado = escolhavar(escolha2, conteudo)

        if resultado is None:
            print("Valor de categoria errada!")
            input("Pressione algo para tentar novamente...\n")
        else:
            dict_[newkey] = resultado
            print(f"'{newkey}: {resultado}' criado com sucesso!\n")
            break
def obter_novo_key_nome(dict_: dict) -> str | None:
    """Valida o nome da chave para não aceitar chaves vazias ou duplicadas."""
    while True:
        newkey = input("Nome da key: ").strip()

        if not newkey:
            print("ERRO! Nenhuma key digitada, tente novamente\n")
            input("Pressione algo para continuar...")
            return None

        if newkey in dict_:
            print(f">>>>> A key '{newkey}' já existe!\n")
            input("Pressione algo para continuar...")
            return None

        return newkey
def exibir_dict(dict_: dict, tamanho_total: int = 13) -> None:
    """Exibe o dicionário formatado com alinhamento de pontos usando for simples."""
    if not dict_:
        print("""
---- Conteúdo do dicionário
          VAZIO!
---------------------------
        """)
        return

    print("----Conteúdo do dicionário")
    for k in dict_:
        qtd_pontos = max(0, tamanho_total - len(k))
        pontos = "." * qtd_pontos
        print(f"{k}{pontos}: {dict_[k]}")
    print("-" * 27)