from random import randint

aleatorio = randint (0, 5)
maquina = 0
usuario = 0

for elemento in range (1, 11):
    numero = int( input(f"{elemento}° Rodada, Digite um numero: "))
    aleatorio = randint (0, 5)
    
    if numero == aleatorio:
        print("Você Acertou")
        usuario = usuario + 1
    else:
        print("Você Errou")
        maquina == maquina + 1
        