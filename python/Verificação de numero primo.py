numero = int(input("Digite um número: "))

primo = True

if numero <= 1:
    primo = False

for i in range(2, numero):

    if numero % i == 0:
        primo = False

if primo:
    print("É número primo")

else:
    print("Não é número primo")
