# 3. Crie uma tupla com o nome dos 12 meses do ano.
# Peça ao usuário um número entre 1 e 12 e mostre o mês correspondente. Se o número for
# inválido, mostre uma mensagem de erro.

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")# tupla com os 12 meses do ano

print("\n====Calendario====")
print("="*30)
num=int(input("Digite um número de 1 à 12 para o mês desejado: "))# pedindo ao usuário um número entre 1 e 12 para mostrar o mês correspondente
if num < 1 or num >  12:# verificando se o número é inválido 
    print("Número inválido! Por favor, digite um número entre 1 e 12.")# mostrando mensagem de erro
else :
    
    num_tupla = tuple(num)# convertendo o número em tupla

    print(f"O mês referente ao numero {num} é: {num_tupla[num-1]}")# mostrando o mês correspondente ao número digitado pelo usuário. "num-1" porque a tupla começa do índice 0.(1-1=0: 2-1=1...)
    #Não consegui fazer funcionar a exibição do mês correspondente usando a tupla diretamente.
    
#======================================================================
#    CORREÇÃO FEITA PELA PROFESSORA PIETRA

# meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho",
        #  "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

# print("---- MESES DO ANO ----")

# while True:
    # numero = int(input("Digite um número entre 1 e 12 para saber o mês correspondente: (Informe -1 para sair)"))

    # if numero == -1:
        # print("Encerrado o sistema!")
        # break

    # if numero >= 1 and numero <= 12:
        # print(f"O mês correspondente é: {meses[numero - 1]}")
    # else:
        # print("Número inválido! Digite novamente entre 1 e 12...")