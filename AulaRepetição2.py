# inicie um loop que vai se repetir enquanto a condição for verdadeira
while True: #True é uma condição booleana que sempre será verdadeira, logo esse loop será infinito até que seja interrompido por um comando break
    nome = input("Usuário: ")
    snha = input("Senha: ")
    
    #condição que faz uma comparação para verificar se ambas condições são verdadeiras
    if nome == "admin" and snha == "1234":
        print("Login realizado com sucesso!")
        break #comando que interrompe imediatamente o loop
    else:
        print("Usuário ou senha incorretos. Tente novamente...")