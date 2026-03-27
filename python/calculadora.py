print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Escolha uma opção: "))

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if op == 1:
    print("Resultado:", n1 + n2)
elif op == 2:
    print("Resultado:", n1 - n2)
elif op == 3:
    print("Resultado:", n1 * n2)
elif op == 4:
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Erro: divisão por zero")
else:
    print("Opção inválida")
