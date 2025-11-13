print("\n====Loja TECHSTORE Senai====")
valor = float(input("Digite o valor total da compra (R$):"))
forma_pagamento = input("Forma de pagamento (dinheiro/cartão débito/cartão de crédito/pix): ")

if forma_pagamento == "dinheiro":
    total = valor * 0.90
    print("Pagamento à vista em dinheiro. Desconto de 10% aplicado.")
elif forma_pagamento == "pix":
    if valor >= 1000:
        total = valor * 0.85
        print("Pagamento via PIX. Desconto de 15% aplicado.")
    elif valor >= 500 and valor < 1000:
        total = valor * 0.90
        print("Pagamento via PIX. Desconto de 10% aplicado.")
    else:
        total = valor * 0.95
        print("Pagamento via PIX. Desconto de 5% aplicado.")
elif forma_pagamento == "débito":        
            total = valor
            print("Pagamento à no cartão de débito!")
elif forma_pagamento == "crédito":
            parcelas = int(input("Em quantas vezes deseja parcelar? "))
            if parcelas <=3: 
                total = valor 
                print("Parcelamento em até 3x sem juros.")
            elif 4 <= parcelas <= 6:
                total = valor*1.10
                print("Parcelamento *4 a 6x com 10 % de juros.")
            else: 
                total= valor*1.20
                print("Parcelamento acima de 6x com 20% de juros.")
else:
    print("Forma de pagamento inv,lida! Tente novamente usando outra opção.")

print(f"Valor final a pagar: R$ {total:.2f}")