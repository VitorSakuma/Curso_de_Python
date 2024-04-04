#DESAFIO 05

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o.

# soma = 0

# for elemento in range(0 , 6):
#     numerointeiro = int(input("Digite um numero: "))
#     if numerointeiro % 2 == 0:
#         soma = soma + numerointeiro

# else:
#     print(f"SOMA de {soma}")
    
# Professor Pedro

soma = 0

for elemento in range (1, 7):
    numero = int(input("Digite um valor: "))
    
    resto = numero % 2
    if resto == 0:
        soma = soma + numero

else:
    print(f" A soma dos valores pares digitados foi igual a {soma}")