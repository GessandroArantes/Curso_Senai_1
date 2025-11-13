# crie um programa que solicite o valor de uma compra. se maior que 100 reais, aplique 10% de desconto. Mostre o valor final. dica: multiplique por 0.9 para aplicar 10% de desconto.
compra = float(input("Digite o valor da compra: R$ "))
if compra>100:
    valor_compra = compra * 0.9
    print("Desconto de 10% aplicado ! \n Valor com desconto: R$ ", compra)
else:
    valor_compra = compra
    print("Valor da compra: R$ ", compra)
    