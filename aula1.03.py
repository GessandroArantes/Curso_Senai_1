nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 8:
    print("Aluno Aprovado com excelência! A média foi: ",media)
elif media >= 5 and media < 8:
    print("Aluno em recuperação! A média foi: ",media)
else:
    print("Aluno reprovado! A média foi: ",media)