# 2) Crie duas listas:
# python
# nomes = []
# salarios = []

# Crie um programa que permita que o usuário cadastre o nome e o salário de cada funcionário.
# O programa deve:
# 1Repetir até que o usuário digite "sair".
#2 Mostrar o total de funcionários cadastrados.
#3 Calcular e exibir a média salarial com sum(salarios) / len(salarios).
#4 Desafio: exibir o maior e o menor salário usando max() e min().

nomes = []
salarios = []

nome = input("Digite o nome do funcionário: (ou 'sair' para encerrar)")

if nome == "sair":
    print("Programa Finalizado!")
    break

nomes.append(nome)

salario = float(input("Digite o salário do funcionário"))

salarios.append(salario)

print(f"O total de funcionários cadastrados é: {len(nomes)}")
print(f"A média salarial dos funcionarios é: {sum(salarios)/len(salarios)}.")
print(f"O maior salario é: {max(salarios)}.")
print(f"O menor salario é: {min(salarios)}.")