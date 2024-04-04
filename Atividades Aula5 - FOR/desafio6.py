#DESAFIO 06

#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input("Digite um termo: "))
razao = int(input("Digite a razao: "))

ultimoTermo = (primeiroTermo + (10 - 1) * razao) + razao

for elemento in range (primeiroTermo, ultimoTermo, razao):
    print(elemento, end= " ->")

else:
    print("FIM")


#print("Vitor", end= "-")
#print("Sakuma")
