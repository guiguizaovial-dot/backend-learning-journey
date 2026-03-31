nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))



if idade < 0:
    print("Idade nao permitida!!!")

elif idade < 18:
    situaçao = "Menor de idade"

else: 
    situaçao = "Maior de idade"

print("Nome:", nome)
print("Idade:", idade)
print("Situaçao", situaçao)
