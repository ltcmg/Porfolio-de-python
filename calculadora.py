num = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
operacao= input("Diugte a operação ( +, -, *, / ): ")

if operacao == "+":
    soma= num + num2 
    print (f"A soma desta operação {soma}")
elif operacao == "-":
    subtracao= num - num2
    print (f'A subtração da operaação é {subtracao}')
elif operacao == "*":
    multiplicacao=  num * num2
    print( f"A multiplicação da operação é {multiplicacao} ")
elif operacao == "/":
    divisao= num / num2
    print(f"A operação da divisão é {divisao}")
else:
    print ("operação inválida")