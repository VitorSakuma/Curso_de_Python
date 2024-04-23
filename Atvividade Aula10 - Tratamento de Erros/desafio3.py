# DESAFIO 03

# Escreva um programa que solicite ao usuário para digitar um
# número inteiro e exiba o resultado da sua raiz quadrada. Lide
# com o erro caso o número seja negativo.

# try:
#     numero = int(input("Por favor, digite um número: "))
#     print(f"{numero}² = {numero**2}")

# except TypeError:
#     prin("Numero inválido")
    

# #
# try:
#     n1 = int(input("Entre com um número inteiro: "))
#     print(math.sqrt(n1))
    
# except:
#     print("Favor inserir um número inteiro válido")
    
    
from math import sqrt
try:
    valor = int(input("Por favor, digite um valor: ")) 
    raizQuadrada = sqrt(valor)
    
except ValueError:
    print("Por favor digite um valor numerico ")
    
else:
    print(raizQuadrada)