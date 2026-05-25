contatos = {}

while True:

    print("\n=== AGENDA ===")
    print("1 - adicionar contato")
    print("2 - mostrar contatos")
    print("3 - sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Nome: ")
        telefone = input("Telefone: ")

        contatos[nome] = telefone

        print("Contato salvo")

    elif opcao == "2":

        for nome in contatos:
            print(nome, "-", contatos[nome])

    elif opcao == "3":
        break

    else:
        print("Opção inválida")
