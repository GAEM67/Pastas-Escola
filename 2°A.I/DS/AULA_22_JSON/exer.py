import os
import json
os.system("cls")

arquivo = "funcionarios.json"
funcionarios = []
while True:
    print("""

------------F-A-Z-B-E-A-R---H-E-L-P-E-R-------------  
0 - SAIR
1 - Cadastrar 
2 - Listar
3 - Buscar
4 - Editar
5 - Excluir
-----------------------------------------------------  
""")
    escolha = int(input("Escolha: "))
    match escolha:
        case 0: 
            print ("PROGRAMA ENCERRADO!!")
            break
        case 1:
     
           

            if os.path.exists(arquivo):
                with open(arquivo, 'r', encoding="utf-8") as f:
                    funcionarios = json.load(f)

            print("\n--- CADASTRO DE FUNCIONÁRIO - FAZBEAR ENTERTAINMENT ---")

            # Solicitar dados do funcionário
            codigo = input("Código(ID): ")
            nome = input("Nome: ")

            print("\nSelecione a Unidade de Trabalho:")
            print("1 - Freddy Fazbear's Mega Pizzaplex")
            print("2 - Edwin Murray Costume Manor")
            print("3 - Freddy Fazbear's Pizza")
            print("4 - Fredbear's Family Diner")

            opcao_unidade = input("Opção (1 a 4): ")

            # Mapeamento das opções para os nomes das unidades
            unidades = {
                "1": "Freddy Fazbear's Mega Pizzaplex",
                "2": "Edwin Murray Costume Manor",
                "3": "Freddy Fazbear's Pizza",
                "4": "Fredbear's Family Diner"
            }

            # Define a unidade selecionada ou uma padrão caso a opção seja inválida
            unidade = unidades.get(opcao_unidade, "Unidade Desconhecida / Não Informada")

            cargo = input("Função: ")
            salario = float(input("Salário: "))

            # Verificar duplicados pelo código/ID
            existe = False
            for func in funcionarios:
                if func["codigo"] == codigo:
                    existe = True
                    break

            if existe:
                print("\n[ERRO] Este código de funcionário já está cadastrado!")
            else:
                funcionario = {
                    'codigo': codigo,
                    'nome': nome,
                    'unidade': unidade,
                    'cargo': cargo,
                    'salario': salario,
                    'status': 'Ativo'
                }

                funcionarios.append(funcionario)

                with open(arquivo, 'w', encoding="utf-8") as f:
                    json.dump(funcionarios, f, indent=4, ensure_ascii=False)

                print(f"\n[SUCESSO] {nome} foi cadastrado(a) na unidade '{unidade}'!")
        case 2:
            arquivo = "funcionarios.json"
            if os.path.exists(arquivo):
                # Abre o arquivo para leitura
                with open(arquivo, 'r', encoding="utf-8") as f:
                    # Converte o json em uma lista de dicionários
                    funcionarios = json.load(f)

                # Verificar se existem registros
                if len(funcionarios) == 0:
                    print("Nenhum funcionário cadastrado na base da Fazbear Entertainment.")
                else:
                    print("------ LISTAGEM DE FUNCIONÁRIOS (FAZBEAR ENTERTAINMENT) ------\n")

                    # Cabeçalho formatado da tabela (ajustado para ID, Nome, Unidade e Cargo)
                    print(f"{'CÓDIGO':8} | {'NOME':20} | {'UNIDADE':35} | {'CARGO':20} | {'SALÁRIO':10}")
                    print(105 * "-")

                    # Percorre todos os registros
                    for func in funcionarios:
                        print(f"{func['codigo']:8} | {func['nome']:20} | {func['unidade']:35} | {func['cargo']:20} | {func['salario']:10.2f}")

            else:
                print("Arquivo de funcionários não encontrado! (Nenhum cadastro efetuado ainda).")
        case 3:
            if os.path.exists(arquivo):
                with open(arquivo, 'r', encoding="utf-8") as f:
                    funcionarios = json.load(f)

                codigo_busca = input("Digite o Código do Funcionário (ID): ")

                encontrado = None

                for func in funcionarios:
                    if func['codigo'] == codigo_busca:
                        encontrado = func
                        break

                if encontrado is not None:
                    print(f"""
--- FUNCIONÁRIO ENCONTRADO ---
Código: {encontrado['codigo']}
Nome: {encontrado['nome']}
Unidade: {encontrado['unidade']}
Cargo: {encontrado['cargo']}
Salário: {encontrado['salario']:.2f} 
Status: {encontrado['status']}
------------------------------
                    """)
                else:
                    print("\n[AVISO] Funcionário não encontrado na base de dados da Fazbear!")
            else:
                print("Arquivo de funcionários não encontrado!")
        case 4:
            print("\n--- EDITAR FUNCIONÁRIO ---")
            codigo_busca = input("Digite o ID do funcionário que deseja editar: ")

            encontrado = None
            for f in funcionarios:
                if f['codigo'] == codigo_busca:
                    encontrado = f
                    break

            if encontrado:
                print(f"\nEditando dados de: {encontrado['nome']}")
                
                novo_nome = input(f"Novo Nome [{encontrado['nome']}]: ")
                if novo_nome.strip():
                    encontrado['nome'] = novo_nome

                print("\nNova Unidade:")
                print("1 - Freddy Fazbear's Mega Pizzaplex")
                print("2 - Edwin Murray Costume Manor")
                print("3 - Freddy Fazbear's Pizza")
                print("4 - Fredbear's Family Diner")
                opcao_unidade = input("Opção (1 a 4) ou Enter para manter: ")
                
                unidades = {
                    "1": "Freddy Fazbear's Mega Pizzaplex",
                    "2": "Edwin Murray Costume Manor",
                    "3": "Freddy's Pizza",
                    "4": "Fredbear's Family Diner"
                }
                if opcao_unidade in unidades:
                    encontrado['unidade'] = unidades[opcao_unidade]

                novo_cargo = input(f"Novo Cargo [{encontrado['cargo']}]: ")
                if novo_cargo.strip():
                    encontrado['cargo'] = novo_cargo

                novo_salario = input(f"Novo Salário [{encontrado['salario']}]: ")
                if novo_salario.strip():
                    try:
                        encontrado['salario'] = float(novo_salario)
                    except ValueError:
                        pass

                with open(arquivo, 'w', encoding="utf-8") as f:
                    json.dump(funcionarios, f, indent=4, ensure_ascii=False)

                print("\n[SUCESSO] Registro atualizado com sucesso!")
            else:
                print("\n[ERRO] Funcionário não encontrado!")
        case 5:
                        
                print("\n--- EXCLUIR FUNCIONÁRIO ---")
                codigo_busca = input("Digite o ID do funcionário a ser removido: ")

                encontrado = None
                for f in funcionarios:
                    if f['codigo'] == codigo_busca:
                        encontrado = f
                        break

                if encontrado:
                    print(f"Funcionário encontrado: {encontrado['nome']} ({encontrado['cargo']})")
                    confirmacao = input("Tem certeza de querer remover funcionario?? (s/n): ").lower()
                    
                    if confirmacao == 's':
                        funcionarios = [f for f in funcionarios if f['codigo'] != codigo_busca]
                        
                        with open(arquivo, 'w', encoding="utf-8") as f:
                            json.dump(funcionarios, f, indent=4, ensure_ascii=False)
                            
                        print("\n[SUCESSO] Funcionário removido")
                    else:
                        print("\nPROCESSO CANCELADO!!")
                else:
                    print("\n[ERRO] Funcionário não encontrado!")
