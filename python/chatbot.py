# ==========================================
# SISTEMA DE CADASTRO DE PRODUTOS
# Versão Corrigida e Melhorada
# ==========================================

# Lista que simula um banco de dados
produtos = []


def gerar_id():
    """Gera um ID automático para cada produto."""
    if not produtos:
        return 1
    return produtos[-1]["id"] + 1


def cadastrar_produto():
    """Realiza o cadastro de um novo produto."""

    print("\n========== CADASTRO DE PRODUTO ==========")

    nome = input("Nome do produto: ").strip()

    if nome == "":
        print("❌ Erro: O nome do produto não pode ficar vazio.")
        return

    # Verifica se já existe um produto com o mesmo nome
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print("❌ Já existe um produto cadastrado com esse nome.")
            return

    try:
        preco = float(input("Preço (R$): ").replace(",", "."))
    except ValueError:
        print("❌ Erro: Digite um preço válido.")
        return

    if preco <= 0:
        print("❌ O preço deve ser maior que zero.")
        return

    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("❌ Erro: Digite uma quantidade válida.")
        return

    if quantidade < 0:
        print("❌ A quantidade não pode ser negativa.")
        return

    produto = {
        "id": gerar_id(),
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

    print("\n✅ Produto cadastrado com sucesso!")


def listar_produtos():
    """Lista todos os produtos cadastrados."""

    print("\n========== LISTA DE PRODUTOS ==========")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"""
ID: {produto['id']}
Nome: {produto['nome']}
Preço: R$ {produto['preco']:.2f}
Quantidade: {produto['quantidade']}
----------------------------------------
""")


def buscar_produto():
    """Busca um produto pelo nome."""

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    nome = input("Digite o nome do produto: ").strip().lower()

    for produto in produtos:
        if produto["nome"].lower() == nome:
            print("\nProduto encontrado!")
            print(f"""
ID: {produto['id']}
Nome: {produto['nome']}
Preço: R$ {produto['preco']:.2f}
Quantidade: {produto['quantidade']}
""")
            return

    print("❌ Produto não encontrado.")


def excluir_produto():
    """Exclui um produto pelo ID."""

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    try:
        codigo = int(input("Digite o ID do produto: "))
    except ValueError:
        print("❌ ID inválido.")
        return

    for produto in produtos:
        if produto["id"] == codigo:

            confirmar = input(
                f"Tem certeza que deseja excluir '{produto['nome']}'? (S/N): "
            ).strip().upper()

            if confirmar == "S":
                produtos.remove(produto)
                print("✅ Produto removido com sucesso.")
            else:
                print("Operação cancelada.")

            return

    print("❌ Produto não encontrado.")


def menu():
    """Exibe o menu principal do sistema."""

    while True:

        print("""
===================================
      SISTEMA DE PRODUTOS
===================================

1 - Cadastrar Produto
2 - Listar Produtos
3 - Buscar Produto
4 - Excluir Produto
5 - Sair

""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            buscar_produto()

        elif opcao == "4":
            excluir_produto()

        elif opcao == "5":
            print("\nSistema encerrado.")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


# Início do programa
menu()
