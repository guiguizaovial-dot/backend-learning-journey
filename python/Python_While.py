numero = int(input("Digite um numero:"))

soma = 0 
contador = 0
maior = numero
menor = numero 


while numero !=0:
    soma = soma + numero
    contador = contador +1 
    
    if numero > maior:
        maior = numero

    if numero < menor :
        menor  = numero 
    
    numero = int(input("Digite um outro numero:"))


print(f"\nA soma total é: {soma}")
print(f"\nQuantidades:{contador}")
print(f"\nMaior numero:{maior}")
print(f"\nO menor numero é:{menor}")
