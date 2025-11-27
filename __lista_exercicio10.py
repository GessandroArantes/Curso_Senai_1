# 10) Função – Crie uma função chamada saudar(nome) que receba um nome e exiba:
# Olá, NOME! Seja bem-vindo(a)!
# Chame a função 3 vezes pedindo nomes ao usuário.

def saudar(nome):
    print("Olá, {nome}! Seja bem-vindo(a).")

    for i in range(3):
     nome = input("Digite seu nome: ")
     saudar(nome)
