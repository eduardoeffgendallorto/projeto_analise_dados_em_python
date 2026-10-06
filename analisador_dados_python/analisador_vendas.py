def registrar_vendas():
    print("\n=== REGISTRO DE VENDAS ===")

    quantidade = int(input("Quantas vendas deseja registrar? "))

    total = 0
    maior = 0
    menor = 0

    for numero in range(1, quantidade + 1):
        valor = float(input("Digite o valor da venda " + str(numero) + ": R$ "))

        total = total + valor

        if numero == 1:
            maior = valor
            menor = valor
        else:
            if valor > maior:
                maior = valor

            if valor < menor:
                menor = valor

    return quantidade, total, maior, menor


def analisar_vendas():
    quantidade, total, maior, menor = registrar_vendas()

    media = total / quantidade

    print("\n=== RELATÓRIO DE VENDAS ===")
    print("Quantidade de vendas:", quantidade)
    print("Faturamento total: R$", round(total, 2))
    print("Maior venda: R$", round(maior, 2))
    print("Menor venda: R$", round(menor, 2))
    print("Média por venda: R$", round(media, 2))

    if media >= 1000:
        print("Análise: o valor médio das vendas está acima de R$ 1.000.")
    elif media >= 500:
        print("Análise: o valor médio das vendas está entre R$ 500 e R$ 1.000.")
    else:
        print("Análise: o valor médio das vendas está abaixo de R$ 500.")


def menu():
    while True:
        print("\n===================================")
        print("       ANALISADOR DE VENDAS")
        print("===================================")
        print("1 - Registrar e analisar vendas")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                analisar_vendas()
            except ValueError:
                print("\nErro: digite somente números válidos.")
        elif opcao == "2":
            print("\nPrograma encerrado.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


menu()
