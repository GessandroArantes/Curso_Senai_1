#Objetivo criar um programa de gerenciamento de notas e mostrar o uso de len(), append(), sum(), remove()

#lista vazia para armazenar as notas
notas = []

print("=====GERENCIADOR DE NOTAS=====")
while True:
    print("\n Menu de opcoes:")
    print("1. Adicionar nota")
    print("2. Remover nota")
    print("3. Mostrar todas notas")
    print("4. Mostrar a quantidade e a media das notas")
    print("5. Sair")

    opcao = int(input("Escolha uma opcao (1-5): "))

    # Se a opcao for = 1, adicionar nota
    # CORREÇÃO 1: '1' deve ser 1 (int) e adicionado notas.append()
    if opcao == 1:
        nota = float(input("Digite a nota a ser adicionada: "))
        notas.append(nota)  # Adição da lógica essencial
        print("Nota adicionada com sucesso!")

    # Remover nota
    # CORREÇÃO 2: '2' deve ser 2 (int)
    elif opcao == 2:
        if len(notas) == 0:
            print("Não há notas para remover.")
        # CORREÇÃO 3: O 'else' deve estar na mesma indentação do 'if' acima
        else:
            print("Notas atuais:", notas)
            remover = float(input("Digite a nota a ser removida: "))
            if remover in notas:
                notas.remove(remover)
                print("Nota removida com sucesso!")
            else:
                print("Essa nota nao existe na lista.")

    # Mostrar todas as notas
    # CORREÇÃO 4: Adiciona a lógica para mostrar as notas.
    elif opcao == 3:
        if len(notas) == 0:
            print("A lista de notas está vazia.")
        else:
            print("Notas cadastradas:", notas)

    # CORREÇÃO 5: Opção 4 - O bloco de cálculo da média estava mal posicionado.
    # Ele precisa de um 'elif opcao == 4:' para ser executado.
    elif opcao == 4:
        if len(notas) == 0:
            print("Nenhuma nota cadastrada ainda para calcular média.")
        else:
            quantidade = len(notas)
            soma = sum(notas)
            media = soma/quantidade
            print(f"Quantidade de notas: {quantidade}")
            print(f"Soma das notas: {soma:.2f}")
            print(f"Média da turma: {media:.2f}")

            if media >= 7:
                print("A turma está com bom desempenho!")
            else:
                print("A turma precisa melhorar.")

    # Sair
    elif opcao == 5:
        print("Encerrando o programa. Até mais!")
        break

    # CORREÇÃO 6: O 'else' final estava sem dois pontos (:)
    else:
        print("Opção inválida. Tente novamente.")
        