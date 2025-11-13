# solicite ao ususuário que informe a hora atual (apenas o número da hora)
hora = int(input("Digite a hora atual (0-23): "))

# estrutura_condicional para verificR O PERIODO DO DIA
if hora <= 12:
    print("Bom dia!")
elif hora > 12 and hora < 18:
        print("Boa tarde!")
else:
    print("Boa noite!")
    