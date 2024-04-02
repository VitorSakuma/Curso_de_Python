#DESAFIO 04
#A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade.
	
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL	
#Até 19 anos: JUNIOR
#Até 24 anos: SÊNIOR
#Acima: MASTER


anoAtleta = int(input("Digite o Ano de Nascimento do Atleta: "))

anoAtual = 2024

idade = anoAtual - anoAtleta
#print (f"O atleta tem {idade} anos")

if idade <= 9:
    print(f"Atleta {idade}, categoria Mirim: ")

elif idade <= 14:
    print(f"Atleta {idade}, categoria Infantil: ") 
    
elif idade <= 19:
    print(f"Atleta {idade}, categoria Junior: ") 

elif idade <= 24:
    print(f"Atleta {idade}, categoria Senior: ") 

elif idade > 24:
    print(f"Atleta {idade}, categoria Master: ") 

