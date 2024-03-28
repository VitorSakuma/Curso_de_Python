#DESAFIO 01

#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numeroComputador = random.randint(0,5)

numeroIntero = int(input("Digite o Numero Inteiro: "))

if numeroComputador == numeroIntero:
    print("Você Acertou")
    
else:
    print("Voce Errou")
    print(f"Valor Escolhido {numeroComputador}")
    