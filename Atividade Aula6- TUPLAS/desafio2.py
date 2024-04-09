# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla.

# Depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na Tupla.

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), )

print(f"Os numeros sorteados foram{numeros}")
print(f"O maior numero sorteado foi: {max(numeros)}")
print(f"O menor numero sorteado foi: {min(numeros)}")