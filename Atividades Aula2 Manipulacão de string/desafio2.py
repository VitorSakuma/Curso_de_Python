#Crie um programa que leia o nome de uma cidade e siga se ela começa ou não com o nome “Santo”.

nomeCidade = input("Digite o nome da Cidade ").upper()

dividirFrase = nomeCidade.split()

nomeCidade = dividirFrase [0]

print("SANTO" in nomeCidade)