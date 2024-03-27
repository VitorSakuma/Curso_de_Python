#Crie um programa que leia o nome completo de uma pessoas e mostre

nome = input("Digite o nome da completo ")

#O nome com todas as letras maiusculas
print(nome.upper())

#O nome com todas as letras minusculas
print(nome.lower())

#Quantas letras ao todo sem considerar espaços
nomeCompleto = nome.replace(" " , "")
print(len(nomeCompleto))

#Quantas letras tem o primeiro nome 

dividirNome = nome.split()

print(len(dividirNome[0]))
