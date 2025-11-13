numeros = () #Criação de tupls com o nome "numeros" que irá quardar números fornecidos pelo usúario

while True: #Início de um loop infinito
    n = int(input("Digite um número (ou -1 para sair): ")) #Solicita ao usuário que digite um número ou 'sair' para encerrar o loop
    if n== -1: #Verifica se o usuário digitou 'sair'
        break #Encerra o loop se o usuário digitou 'sair'
    numeros += (n,) #Adiciona o número digitado à tupla "numeros"
    
    if len (numeros) > 0:
        print("\n====== RESULTADOS ======") #Imprime um cabeçalho para os resultados
        print(f"Números digitados: {numeros}") #Exibe os números digitados pelo usuário
        print(f"Quantidade de números: {len(numeros)}") #Exibe a quantidade de números digitados
        print(f"Soma: {sum(numeros)}") #Exibe a soma dos números digitados
        print(f"Maior numero: {max(numeros)}") #Exibe o maior número digitado
        print(f"Menor número: {min(numeros)}") #Exibe o menor número digitado: #Verifica se a tupla "numeros" contém elementos
        
        media = sum(numeros) / len(numeros) #Calcula a média dos números digitados
        
        if media >= 50: #Verifica se a média é maior ou igual a 50
            print(f"A média: {media:.2f} -> Alta!") #Exibe a média com uma mensagem indicando que é alta
        else: #Caso contrário
            print(f"A média: {media:.2f} -> Baixa!") #Exibe a média com uma mensagem indicando que é baixa > 0: #Verifica se a tupla "numeros" contém elementos
    else: #Caso contrário
        print("Nenhum número foi adicionado.") #Informa que nenhum número foi adicionado
        