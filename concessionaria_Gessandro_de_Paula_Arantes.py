
# Requisitos Técnicos do Sistema:
# • Cadastro Inicial do Cliente
# → Solicitar nome, telefone e saldo inicial.
# → Armazenar esses dados em um dicionário.

#  Venda de Veículos (Cliente → Empresa)
# • O cliente informa marca e modelo do veículo.
# • O sistema consulta o valor FIPE (armazenado em um dicionário).
# • A proposta da empresa deve ser o valor FIPE com 12% de desconto.
# • Se o cliente aceitar, o valor é adicionado ao saldo e o veículo entra na lista da empresa.
# • Exemplo:
# Valor FIPE: R$ 50.000
# Proposta: R$ 44.000 (–12%)
#  Aluguel de Veículos (Cliente ← Empresa)
# • O cliente escolhe um veículo disponível para locação (lista pré-definida).
# • Informa o número de dias desejado.
# • O valor do aluguel é R$77 por dia.
# • O sistema verifica se o saldo é suficiente e, se confirmado,
# o desconta o valor,
# o remove o veículo da lista de disponíveis.
# • Exemplo:
# Aluguel de 5 dias → 5 × 77 = R$ 385
#  Compra de Veículos (Cliente ← Empresa)
# • O cliente escolhe um veículo da lista de veículos à venda.
# • O sistema consulta o valor FIPE e adiciona 25% de acréscimo.
# • Se o saldo for suficiente, o valor é descontado e o veículo é removido da lista.
# • Exemplo:
# Valor FIPE: R$ 60.000
# Preço de venda: R$ 75.000 (+25%)
# Regras Gerais:
# • O sistema deve permitir voltar ao menu principal a qualquer momento.
# • Se o saldo for insuficiente, a operação será cancelada automaticamente.
# • Usar um dicionário “tabela FIPE” com pelo menos 5 modelos e valores.
# • Usar funções para cada funcionalidade (vender(), alugar(), comprar(), menu() etc.).
# • Utilizar estrutura de repetição para manter o programa em execução até o usuário escolher “Sair”.

cliente = {
            "nome": input("Digite seu nome: "),
            "celular":input("Número para contato: "),
            "saldo_inicial": float(input("Digite seu saldo inicial R$: "))
            }
  
