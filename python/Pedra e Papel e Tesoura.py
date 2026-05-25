import random

opcoes = ["pedra", "papel", "tesoura"]

computador = random.choice(opcoes)

print("=== PEDRA PAPEL TESOURA ===")

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

print("Computador escolheu:", computador)

if jogador == computador:
    print("Empate!")

elif jogador == "pedra" and computador == "tesoura":
    print("Você venceu!")

elif jogador == "papel" and computador == "pedra":
    print("Você venceu!")

elif jogador == "tesoura" and computador == "papel":
    print("Você venceu!")

else:
    print("Computador venceu!")
