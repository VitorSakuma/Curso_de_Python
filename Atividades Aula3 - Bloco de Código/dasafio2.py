#DESAFIO 02

# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$ 7,00 por cada Km acima do limite.
import random

velocidade1  = int(input(f"Digite uma velocidade: "))
velocidadePermitida = 80


if velocidade1 <= 80:
    print(f"Pode passar")    
else:
    multa = (velocidade1-velocidadePermitida)*7
    print(f"velocidade superior a 80km/h, Multa de R$ {multa}")
    