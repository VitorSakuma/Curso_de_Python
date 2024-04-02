#DESAFIO 06
#Crie um programa que faça o computador jogar Jokenpô com você: 

#pedra, papel, tesoura


from random import choice

opcoes = ["PEDRA" , "PAPEL" , "TESOURA"]
escolhaMaquina = choice(opcoes)
print(escolhaMaquina)

escolhaUsuario = input("informe a sua escolha: ") . upper()
if escolhaMaquina ==escolhaUsuario:
    print(f"Ambos escolheu o mesmo {escolhaMaquina}, portanto EMPATE")
    
elif escolhaMaquina == "PEDRA" and escolhaUsuario == "TESOURA":
    print(f"A maquina escolheu {escolhaMaquina}, portanto ela venceu")

elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PAPEL":
    print(f"A maquina escolheu {escolhaMaquina}, portanto ela venceu")

elif escolhaMaquina == "PAPEL" and escolhaUsuario == "PEDRA":
    print(f"A maquina escolheu {escolhaMaquina}, portanto ela venceu")
    
elif escolhaMaquina == "TESOURA" and escolhaUsuario == "PEDRA":
    print(f"Voce escolheu {escolhaUsuario}, portanto voce venceu")
    
elif escolhaMaquina == "PAPEL" and escolhaUsuario == "TESOURA":
    print(f"Voce escolheu {escolhaUsuario}, portanto voce venceu")

elif escolhaMaquina == "PEDRA" and escolhaUsuario == "PAPEL":
    print(f"Voce escolheu {escolhaUsuario}, portanto voce venceu")
    
else:
    print("A opção esta incorreta")
 
