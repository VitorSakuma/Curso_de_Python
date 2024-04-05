#DESAFIO 01

#Faça um jogo, onde o computador vai “pensar” em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

computador = random.randint(0,10)
palpite = 1
valorPalpite = 1

while True:
     jogador = int(input("Entre com um palpite inteiro entre 0 e 10: "))
    
     if (jogador < 0 or jogador > 10):
         print("Favor entrar com um palpite entre 0 a 10: ")
         palpite = palpite + valorPalpite
         continue    
    
     else:
         if computador == jogador:
             print(f"Parabens você acertou o palpite {computador} no {palpite}º tentativa.")
             break
         else:
             print("Tente novamente um palpite: ")
             palpite = palpite + valorPalpite
            
             continue