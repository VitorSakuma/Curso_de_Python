# DESAFIO 02

# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultado aleatórios. Guarde esses resultados em um
# dicionário . No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter


meuDicionario = {
    "jogador 1" : randint(1, 6),
    "jogador 2" : randint(1, 6),
    "jogador 3" : randint(1, 6),
    "jogador 4" : randint(1, 6)
}


for k, v in meuDicionario.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
    
    # print("Em ordem crescente")
    
# sorted(iterable, key==key, reverse=reverse)
# sorted(quem?, qual a chave, quem inverte)

ranking = sorted(meuDicionario.items(), key=itemgetter(1), reverse=True)
print(ranking)
