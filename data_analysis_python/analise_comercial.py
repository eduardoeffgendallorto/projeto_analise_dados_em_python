def calcular_resultados(faturamento, despesas, quantidade):
    lucro = faturamento - despesas
    ticket_medio = faturamento / quantidade
    margem = (lucro / faturamento) * 100

    return lucro, ticket_medio, margem


def analisar_desempenho(lucro, margem):
    if lucro < 0:
        return "PREJUIZO", "As despesas foram maiores que o faturamento."
    elif margem >= 50:
        return "EXCELENTE", "A margem de lucro esta muito boa."
    elif margem >= 20:
        return "BOM", "A empresa apresentou uma margem de lucro positiva."
    else:
        return "ATENCAO", "A margem de lucro esta baixa."


print("========================================")
print("       SISTEMA DE ANALISE COMERCIAL")
print("========================================")

while True:
    print("\n1 - Registrar vendas")
    print("2 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        try:
            quantidade = int(input("\nQuantas vendas deseja registrar? "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
                continue

            faturamento = 0
            maior = 0
            menor = 0

            for numero in range(1, quantidade + 1):
                valor = float(input("Digite o valor da venda " + str(numero) + ": R$ "))
                faturamento = faturamento + valor

                if numero == 1:
                    maior = valor
                    menor = valor
                else:
                    if valor > maior:
                        maior = valor

                    if valor < menor:
                        menor = valor

            despesas = float(input("Digite o total de despesas: R$ "))

            if despesas < 0:
                print("As despesas nao podem ser negativas.")
                continue

            lucro, ticket_medio, margem = calcular_resultados(
                faturamento, despesas, quantidade
            )

            desempenho, analise = analisar_desempenho(lucro, margem)

            print("\n========== RELATORIO COMERCIAL ==========")
            print("Vendas realizadas:", quantidade)
            print("Faturamento:       R$", round(faturamento, 2))
            print("Despesas:          R$", round(despesas, 2))
            print("Lucro:             R$", round(lucro, 2))
            print("Ticket medio:      R$", round(ticket_medio, 2))
            print("Maior venda:       R$", round(maior, 2))
            print("Menor venda:       R$", round(menor, 2))
            print("Margem de lucro:   ", round(margem, 2), "%")
            print("Desempenho:        ", desempenho)
            print("Analise:           ", analise)
            print("=========================================")

        except ValueError:
            print("Erro: digite somente valores numericos.")

    elif opcao == "2":
        print("\nPrograma encerrado.")
        break

    else:
        print("Opcao invalida. Tente novamente.")
