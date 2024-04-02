#DESAFIO 03

#Crie um programa que leia duas notas entre 0 a 10 de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.

#Média abaixo de 5.0: REPROVADO

#Média entre 5.0 a 6.9: RECUPERAÇÃO

#Média igual ou superior a 7.0: APROVADO

nota1 = float(input("Digite a primeira nota entre 0 a 10: "))
nota2 = float(input("Digite a segunda nota entre 0 a 10: "))


if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    
    mediaAluno = (nota1 + nota2) / 2

    if mediaAluno >= 7 :
        print(f"Aluno Aprovado com ")

    elif mediaAluno >= 5 :
        print(f"Aluno em Recuperação: ") 

    else:
        print(f"Aluno Reprovado")
 
else:
     print("Por favor digite uma nota valida")