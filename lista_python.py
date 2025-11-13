#Exemplo de lsta
##print(numeros)#Imprimindo a lista completa
# print(numeros[0])#Acessando a lista e pegando o primeiro valor da lista
# numeros[1] = 15 #Alterando o valor do segundo item da lista
# numeros[3] = 25 #Alterando o valor do quarto item da lista
# print(numeros) #Imprimindo a lista com os valores alterados

# ========================================================================


# Exemplo de Tupa
# coordenadas = (3,7)
# print(coordenadas[0]) #Acessando o primeiro valor da tupla
# print(coordenadas[1]) #Acessando o segundo valor da tupla   
# coordenadas[0] = 13
# coordenadas[1] = 17
# print(coordenadas) #Imprimindo a tupla com os valores alterados


# ========================================================================

# Append() - Metodo que serve para adicionar um novo elemento ao final da lista
# remove() - Metodo que serve para remover um elemento especifico da lista
paises = ["Brasil", "Argentina"]
print(paises) #Imprimindo a lista original
paises.append("Russia") #Adicionando um novo elemento ao final da lista
print(paises) #Imprimindo a lista com o novo elemento adicionado
paises.remove("Argentina") #Removendo o elemento "Argentina" da lista
print(paises) #Imprimindo a lista com o elemento removido

if "Italia" in paises:
    paises.remove("Italia")
else:
        print("Italia nao encontrada na lista")
        
        
        # ========================================================================
        #len() - metodo que serve para contagem de caracteres, numeros, letras, palavras....
        #sum() - metodo que serve para somar valores numericos em uma lista
       
        numeros = [10, 20, 30]
        print("Quantidade de numeros na lista:", len(numeros)) #Imprimindo a quantidade de elementos na lista
       
        notas = [7.5, 8.5, 10]
        print("Soma das notas:", sum(notas)) #Imprimindo a soma dos valores na lista
        print(f"A media das notas e: {sum(notas) / len(notas):.2f}")
        