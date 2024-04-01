# DESAFIO 03

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

import random

distancia1  = int(input(f"Digite uma velocidade: "))


if distancia1 <= 200:    
    valor = (distancia1 *0.50)
    print(f"Valor a ser cobrado é R$ {valor}")    
else:
    valor = distancia1*0.45
    print(f"Valor a ser cobrado é R$ {valor}")   
    