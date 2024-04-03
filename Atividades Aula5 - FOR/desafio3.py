#DESAFIO 03

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

total = 0  
for numeroImpares in range(1, 501):  
    if numeroImpares % 2 != 0:  
        if numeroImpares % 3 == 0:  
            total = total + numeroImpares
            print(numeroImpares)  
else:
    print(f"O total da soma dos numeros impar e multiplos de 3  entre 1 a 500 é {total}")
