idade = int(input("Digite uma idade: "))

if idade <= 12:
    print("Ele é uma criança")

elif idade <= 17:
    print("Ele é adolescente")

elif idade <= 59:
    print("Ele é um adulto")

else:
    print("Ele é idoso")
