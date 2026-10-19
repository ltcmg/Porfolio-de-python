print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")


try:
     escolha = int(input("Escolha uma operação: "))
     num1= int(input("Digite um número: "))
     num2= int (input("digite o seugundo numero: "))

except ValueError:
    print("Erro! Digite apenas números inteiros válidos.")

except ZeroDivisionError:
    print("Erro! Não é possível dividir por zero.")

if escolha == 1:
    soma= num1 + num2
    print(f"Resultado: {soma}")

elif escolha ==2:
    subtrair= num1 - num2
    print(f"Resultado: {subtrair}")

elif escolha ==3:
    multiplica= num1 * num2
    print(f"Resultado: {multiplica}")
elif escolha ==4:
    dividir= num1 / num2
    print(f"Resultado: {dividir}")
else:
    (f"opção inválida.")


