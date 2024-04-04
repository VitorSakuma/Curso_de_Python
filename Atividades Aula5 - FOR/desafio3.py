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
    

"""
soma = 0
    
for elemento in range (1, 501, 1):
    multiplo3 = elemento % 3
    impar = elemento % 2
    
    if multiplo3 == 0 and impar ==1:
        print(f"O numero {elemento} é Multiplo de 3")
        soma = soma + elemento
else:
    print(f"Valor da soma dos numero impar multiplos de 3 é: {soma} ")

"""