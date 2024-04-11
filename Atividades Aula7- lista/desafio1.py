# DESAFIO 01

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# lstValores = []

# for n in range(1,6):    
#     lstValores.append(int(input(f"Entre o {n}º número: ")))    
    
# print(f"O maior valor da lista é {max(lstValores)} e sua posição é {lstValores.index(max(lstValores))}")
# print(f"O menor valor da lista é {min(lstValores)} e sua posição é {lstValores.index(min(lstValores))}")


minhaLista= []

for i in range(0,5):
    numero = int(input("Digite o valor numerico: "))
    minhaLista.append(numero)
    
print(minhaLista)

maiorNumero = max(minhaLista)
menorNumero = min(minhaLista)

print(f"o maior valor sera, {maiorNumero} e a sua posição, {minhaLista.index(maiorNumero)}" , end=" ")
print(f"o menor valor sera, {menorNumero} e a sua posição, {minhaLista.index(menorNumero)}" , end=" ")

