#DESAFIO 05

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o.

soma = 0

for elemento in range(0 , 6):
    numerointeiro = int(input("Digite um numero: "))
    if numerointeiro % 2 == 0:
        soma = soma + numerointeiro

else:
    print(f"SOMA de {soma}")