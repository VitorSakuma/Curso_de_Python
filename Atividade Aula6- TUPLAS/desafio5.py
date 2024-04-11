# DESAFIO 05

# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.

# No final, mostre uma listagem de preços, organizando os dados em
# forma tabular.

# from tabulate import tabulate

# produtos = (["Bala","0.30"],["suco","4.10"],["Sorvete","32.30"],["Paçoca","1.5"],["M&M","11.30"],["Milka","18.30"])            
# print(tabulate(produtos, headers=["Produto", "Preço"]))

itens = ('Arroz',26, 'Feijão',8, 'Macarrão',3, 'Banana',40)
print(itens)
#print(len(itens))

for i in range (0, len(itens)):
    if type(itens[i]) is str:
        print(f"Produto: {itens[i]:.<10}....Preço: R${itens[i+1]},00")
        
#print(type(itens))


############# OU  ###########

from tabulate import tabulate

produtos = [['Bala','0,30'], ['Suco','1,00'],['Salgado','3,00'], ['Sorvete','5,00'] ]
tuplaprodutos = tuple(produtos)
print(tabulate(tuplaprodutos, headers=["Produto", "Preço"]))