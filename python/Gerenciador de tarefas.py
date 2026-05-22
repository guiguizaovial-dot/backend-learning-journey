tarefas = []

while True:

    print("\n=== LISTA DE TAREFAS ===")
    print("1 - adicionar tarefa")
    print("2 - mostrar tarefas")
    print("3 - remover tarefa")
    print("4 - sair")

    opcao = input("Escolhe uma opção: ")

    if opcao == "1":
        tarefa = input("Escreve a tarefa: ")
        tarefas.append(tarefa)
        print("ok, tarefa adicionada")

    elif opcao == "2":

        if len(tarefas) == 0:
            print("não tem tarefas ainda")

        else:
            print("\nsuas tarefas:")
            for i in range(len(tarefas)):
                print(str(i+1) + " - " + tarefas[i])

    elif opcao == "3":
        numero = int(input("qual número quer apagar? "))

        if numero > 0 and numero <= len(tarefas):
            tarefas.pop(numero - 1)
            print("tarefa removida")
        else:
            print("número inválido")

    elif opcao == "4":
        print("saindo...")
        break

    else:
        print("opção inválida")
