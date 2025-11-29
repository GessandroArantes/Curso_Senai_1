# 11) Função + Lista – Crie uma função chamada calcular_media(lista_notas). A função deve 
# retornar a média dos valores. 
# No programa principal: 
# • Peça 4 notas ao usuário 
# • Coloque numa lista 
# • Use a função para calcular a média 
# • Exiba o resultado

nota=[]
def informa_nota():
  for i in range(4):
   notas = float(input(f"Didite a {i+1}ª nota: "))
   nota.append(notas)
informa_nota ()

def media_nota(nota):
    soma = sum(nota)          # soma todos os valores da lista
    quantidade = len(nota)    # conta quantos elementos tem na lista
    media = soma / quantidade        # calcula a média
    print (f" --> {media}")
                # retorna o resultado
media_nota(nota) 