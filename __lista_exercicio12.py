# 12) Função + Dicionário + Repetição - Crie uma função cadastrar_pessoa() que: 
# • Peça nome 
# • Peça idade 
# • Peça cidade 
# • Retorne um dicionário com esses dados 
# No programa principal: 
# • Use um while para cadastrar várias pessoas 
# • Cada pessoa deve ser guardada dentro de uma lista de dicionários 
# • Pare quando o usuário digitar “sair” 
# • Ao final, exiba todos os cadastros organizados



print("="*90)
print("=== CADASTRO DE PESSOAS ===")
def cadastrar_pessoas():
    nome = input("Digite o nome: ").title()
    idade = int(input("Digite a idade: "))
    cidade = input("Digite o nome da cidade: ").title()

    cadastro = {
     "nome": nome,
     "idade": idade,
     "cidade": cidade

     }
    return cadastro

lista_cadastro = []

while True:
    cadastro = cadastrar_pessoas()
   
        
    sair = input("Para encerrar digite a palavra (Sair) ou ENTER para continuar:").title() 
    if sair == 'Sair':
        print("Encerrando os cadastros de nomes no sistema!")
        break

    
    lista_cadastro.append(cadastro)
    print("==== CADASTROS DE NOMES ====\n")
for i, item  in enumerate(lista_cadastro, start=1):
    print(f" Cadastro:\nNome: {item['nome']}. \nIdade: {item['idade']}. \nCidade: {item['cidade']}.\n\n")



































