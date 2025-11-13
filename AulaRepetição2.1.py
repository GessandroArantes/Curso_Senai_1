print("\nCadastro de Usuário\n")
usuario_cadastrado = input("Crie seu nome de usuário: ").strip().lower()


# print("\nUsário cadastrado com sucesso!\n")

# inicie um loop que vai se repetir enquanto a condição for verdadeira
while True: #True é uma condição booleana que sempre será verdadeira, logo esse loop será infinito até que seja interrompido por um comando break
    senha_cadastrada = input("Crie sua senha de usúario (máx. 8 caracteres): ").strip()
    
    if len(senha_cadastrada) <= 8:
        print("\nUsuario cadastrado com sucesso!\n")
        break
    else:
        print("Senha muito longa! Digite uma senha com até 8 caracteres.n")
    print("--- Login ---")
    nome = input("Usuário: ").strip().lower()
    snha = input("Senha: ").strip()
    
    #condição que faz uma comparação para verificar se ambas condições são verdadeiras
    if nome == usuario_cadastrado and snha == senha_cadastrada:
        print(f"Login realizado com sucesso!\n Seja Bem-vindo(a) {nome}")
        break #comando que interrompe imediatamente o loop
    else:
        print("Usuário ou senha incorretos. Tente novamente...")