try:
    num1=int(input("Digite o primeiro numero: "))
    num2=int(input("Digite o segundo numero: "))
    divi= num1/num2
    print(f'O Respultado dos numero pela divisão é {divi}')
except ValueError:
    print(f"Erro! Digite apenas números inteiros.")
except ZeroDivisionError:
    print (f"Não pode dividir por zero")