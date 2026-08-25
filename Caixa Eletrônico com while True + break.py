saldo = 1000

while True:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Seu saldo é:", saldo)

    elif opcao == 2:
        deposito = int(input("Digite o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            print("Depósito realizado!")
            print("Seu novo saldo é:", saldo)
        else:
            print("Valor de depósito inválido!")

    elif opcao == 3:
        saque = int(input("Digite o valor do saque: "))

        if saque > 0 and saque <= saldo:
            saldo -= saque
            print("Saque realizado!")
            print("Seu novo saldo é:", saldo)
        else:
            print("Saque inválido ou saldo insuficiente!")

    elif opcao == 4:
        print("Obrigado por utilizar o caixa eletrônico!")
        break

    else:
        print("Opção inválida!")
