# DESAFIO 05

# Faça um programa que leia nome e peso de varias pessoas,
# guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.

# B) Uma listagem com as pessoas mais pesadas.

# C) Um listagem com as pessoas mais leves

dadosPessoas = []
dadosCadastro = []

continuacao = 'S'

while True:
    dadosCadastro.append(input("nome:"))
    dadosCadastro.append(int(input("Peso")))
    dadosPessoas.extend(dadosCadastro)
    continuacao = input("Deseja continuar? S - SIM N - NÃO: ").upper()
    
    if continuacao ==  'N':
        break
print(dadosPessoas)
print(dadosCadastro)

nomePessoas = []
pesoPessoas = []
continuacao = 'S'
salvar = []

while True:
    nomePessoas.append((input("Digite o nome: ")))
    pesoPessoas.append((input('Digite o peso da pessoa cadastrada anteriormente: ')))
    continuacao = input("Deseja continuar? S - SIM N - NÃO: ").upper()
    
    salvar.append(pesoPessoas+nomePessoas)
    nomePessoas.clear()
    pesoPessoas.clear()
    # print(f'{nomePessoas}verif')
    # print(f'{pesoPessoas}verif')
    if continuacao ==  'N':
        break
print(salvar)