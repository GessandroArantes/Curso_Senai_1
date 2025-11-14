# 1. Crie uma tupla chamada nomes com 5 nomes de colegas.
# Depois, exiba:
# ● O primeiro e o último nome da tupla.
# ● A quantidade total de nomes.



nomes = ("João", "Maria", "José", "Carlos", "Eva")# tupla com 5 nomes
print("\n====Lista de Nomes dos Colegas====")
print("="*75)
print(f"Lista de nomes dos colegas:\n{nomes}")# exibindo a lista completa de nomes
print(f"Primeiro nome: {nomes[0]}")# exibindo o primeiro nome
print(f"O ultimo nome é: {nomes[4]}")# exibindo o ultimo nome
print(f"A quantidade de nomes é: {len(nomes)}")# exibindo a quantidade total de nomes
print("="*75)

#=====================================================================================================

#    CORREÇÃO FEITA PELA PROFESSORA PIETRA

# nomes = ("ana", "breno", "carlos", "daniela", "enzo")

# print("=== LISTA DE NOMES ===")
# print(nomes)

# print(f"Primeiro nome - {nomes[0]}")
# print(f"Último nome - {nomes[-1]}")
# print(f"A quantidade total de nomes é: {len(nomes)}")

#=====================================================================================================
# *Segunda forma para resolver o problema

#nomes = ("ana", "breno", "carlos", "daniela", "enzo") tupla com nomes já definidos
# nomes = () #tupla vazia

# print("=== LISTA DE NOMES ===")
#print(nomes) mostra a tupla com os nomes

#Estrutura de repetição que vai rodar 5 vezes pedindo nomes
# for i in range(5):
    # nome = input(f"Digite o {i+1}º nome: ")
    # nomes += (nome, ) #adiciona os nomes informados pelo usuário à tupla

# print(f"Nomes cadastrados: {nomes}")
# print(f"Primeiro nome - {nomes[0]}")
# print(f"Último nome - {nomes[-1]}")
# print(f"A quantidade total de nomes é: {len(nomes)}")