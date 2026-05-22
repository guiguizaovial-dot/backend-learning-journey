saldo = 0

while True:

    print("\n=== BANCO ===")
    print("1 - depositar")
    print("2 - sacar")
    print("3 - ver saldo")
    print("4 - sair")

    opcao = input("opção: ")

    if opcao == "1":
        valor = float(input("quanto quer depositar? R$ "))
        saldo = saldo + valor
        print("deposito feito")

    elif opcao == "2":
        valor = float(input("quanto quer sacar? R$ "))

        if valor <= saldo:
            saldo = saldo - valor
            print("saque feito")
        else:
            print("não tem saldo suficiente")

    elif opcao == "3":
        print("seu saldo é: R$", saldo)

    elif opcao == "4":
        print("fechando sistema...")
        break

    else:
        print("opção errada")
