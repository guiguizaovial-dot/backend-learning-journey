estoque = {}

while True:

    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1 - adicionar produto")
    print("2 - mostrar estoque")
    print("3 - sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))

        estoque[produto] = quantidade

        print("Produto adicionado!")

    elif opcao == "2":

        print("\nESTOQUE:")

        for produto in estoque:
            print(produto, "-", estoque[produto])

    elif opcao == "3":

        print("Saindo...")
        break

    else:

        print("Opção inválida")
