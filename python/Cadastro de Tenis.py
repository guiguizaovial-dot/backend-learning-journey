while True:
    print("1 - CADASTRAR TENIS:")
    print("2 - MOSTRAR TENIS:")
    print("3 - SAIR")
    
    opcao = input("Escolha a sua opção:")

    if opcao =="1":
        Marca = input("Digite a marca do tenis:")
        Modelo = input("Digite o modelo do tenis:")
        Tamanho = input("Digite o tamanho do tenis:")
        Preço = input("Digite a preço do tenis:")
        
        
        arquivo = open("tenis.txt", "a")
        arquivo.write(Marca + "\n")
        arquivo.write(Modelo + "\n")
        arquivo.write(Tamanho + "\n")
        arquivo.write(Preço + "\n")
        arquivo.close()

    elif opcao == "2":
        arquivo = open("tenis.txt", "r")
        print(arquivo.read())
        arquivo.close

    elif opcao == "3":
        print("Ja encerramos o programa")

    else:
        print("Opçao invaida!!")
