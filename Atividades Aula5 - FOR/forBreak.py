from random import *


escolhaMaquina = randint (1, 20)
print(escolhaMaquina)

for elemento in range (1, 11, 1): 
    
    escolhaUsuario = int( input(f"{elemento}° Rodada, Digite um numero: "))   
    
    if escolhaUsuario == escolhaMaquina:
        print("VOCE VENCEU")
        break

else:
    print("Maquina Ganhou")

        
print("Acabou o Jogo")
    