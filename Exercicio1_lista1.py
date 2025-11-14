# 1) Crie um programa que permita que o usuário cadastre nomes de alunos em uma lista.
# ● O programa deve repetir até que o usuário digite "sair".
# ● Ao final, o programa deve:
# ○ Mostrar quantos alunos foram cadastrados.
# ○ Exibir a lista completa de nomes.
# 💡 Dica: use while True, break e append.


lista_nomes=[]
print("--- PROGRAMA DE CADASTRO DE ALUNOS ---")
print("\n--- CASO QUEIRA ENCERRAR DIGITE SAIR ---")
print("_"*50)

while True:#inicia o loop infinito 
    nomes=input("Digite o nome do aluno ou (sair) ").strip()#.strip() apaga espaços desnecessarios
    
    if nomes.lower()== "sair":
        print("Encerrando o programa!")
        break#Se o nome digitado for "sair" (em qualquer caixa, graças ao .lower()), a instrução break é executada, o que interrompe o loop while.
    lista_nomes.append(nomes)
   
       
print(f"Aluno {lista_nomes} adicionado com sucesso!")
print(f"A quantidade de nomes adicionado foi {len(lista_nomes)}")
        