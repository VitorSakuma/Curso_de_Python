#DESAFIO 03

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

variavel = 0  # Contador de soma
for numeroImpares in range(1, 501):  # de 1 até 500
    if numeroImpares % 2 != 0:  # Ímpares
        if numeroImpares % 3 == 0:  # Ímpares múltiplos de 3
            variavel += numeroImpares  # soma = soma + num
print("A soma dos múltiplos é")


#{}.".format(variavel))