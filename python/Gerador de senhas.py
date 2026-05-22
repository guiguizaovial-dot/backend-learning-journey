import random
import string

print("=== GERADOR DE SENHA ===")

tamanho = int(input("Quantos caracteres você quer na senha? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ""

for i in range(tamanho):
    senha = senha + random.choice(caracteres)

print("\nSua senha ficou assim:")
print(senha)
