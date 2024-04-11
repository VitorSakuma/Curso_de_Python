meuDicionario = {
    "Nome": "Nami",
    "Sobrenome": "Jafet",
    "Idade": 67
}

print(meuDicionario)
print(meuDicionario.items())
print(meuDicionario.keys())
print(meuDicionario.values())
print(meuDicionario["Sobrenome"])


# ##lista de Dicionario

personagens = [
    {
        "Nome": "Bob",
        "Sobrenome": "Esponja",
        "Idade": 10
    },
    
     {
        "Nome": "Jhony",
        "Sobrenome": "Bravo",
        "Idade": 35
    }
]

# acessando apenas o primeiro registro (primeiro dicionario na lista)

primeiroRegistro = personagens[0]
# print(primeiroRegistro)
# print(personagens)
# print(personagens[0].get())

#Acessando apenas um valor especifico - Resultado = Bob

print(primeiroRegistro["Nome"])
#ou
print(personagens[0].get("Nome"))