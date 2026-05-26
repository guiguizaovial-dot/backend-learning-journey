filmes = []

while True:

    print("\n=== SISTEMA DE FILMES ===")
    print("1 - adicionar filme")
    print("2 - mostrar filmes")
    print("3 - sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Nome do filme: ")
        nota = input("Nota do filme: ")
        genero = input("Gênero: ")

        filme = {
            "nome": nome,
            "nota": nota,
            "genero": genero
        }

        filmes.append(filme)

        print("Filme adicionado!")

    elif opcao == "2":

        print("\nFILMES:")

        for filme in filmes:

            print("\nNome:", filme["nome"])
            print("Nota:", filme["nota"])
            print("Gênero:", filme["genero"])

    elif opcao == "3":

        break

    else:

        print("Opção inválida")
