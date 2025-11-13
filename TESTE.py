# Inicializa a lista vazia para armazenar os nomes dos alunos
lista_alunos = []

print("Bem-vindo ao programa de cadastro de alunos!")
print("Digite 'sair' a qualquer momento para finalizar o cadastro.")
print("-" * 35)

# O loop principal para cadastrar os nomes
while True:
    # Solicita o nome do aluno ao usuário
    nome = input("Digite o nome do aluno (ou 'sair'): ").strip()

    # Verifica se o usuário deseja sair
    if nome.lower() == "sair":
        # Interrompe o loop while
        break
    
    # Verifica se o nome não está vazio antes de adicionar
    elif nome:
        # Adiciona o nome à lista
        lista_alunos.append(nome)
        print(f"✅ Aluno '{nome}' cadastrado com sucesso.")
    
    # Caso o usuário digite apenas espaços ou a entrada seja vazia
    else:
        print("⚠️ Por favor, digite um nome válido.")
        
    print("-" * 35)

# --- Processamento e Exibição dos Resultados ---

# 1. Mostrar quantos alunos foram cadastrados
total_alunos = len(lista_alunos)
print("\n" + "=" * 40)
print(f"🎉 **FIM DO CADASTRO!**")
print(f"Total de alunos cadastrados: **{total_alunos}**")
print("=" * 40)

# 2. Exibir a lista completa de nomes
if total_alunos > 0:
    print("\n📚 **Lista Completa de Nomes:**")
    # Itera sobre a lista para exibir cada nome
    for i, aluno in enumerate(lista_alunos, 1):
        print(f"{i}. {aluno}")
else:
    print("\n😔 Nenhum aluno foi cadastrado na lista.")