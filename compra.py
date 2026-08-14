compra = float(input("Digite o valor da sua compra: R$ "))

if compra >= 500.00:
    desconto = compra * 0.10
    valor_final = compra - desconto
    print(f"Valor do desconto: R$ {desconto}")
    print(f"Valor final da compra: R$ {valor_final}")

elif compra > 100.00:
    desconto = compra * 0.20
    valor_final = compra - desconto
    print(f"Valor do desconto: R$ {desconto}")
    print(f"Valor final da compra: R$ {valor_final}")

else:
    desconto = 0
    valor_final = compra
    print("Sem desconto")
    print(f"Valor final da compra: R$ {valor_final}")