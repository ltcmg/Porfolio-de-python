try:
    n1= int(input("digite um número inteiro: "))
    n2= int(input("digite o segundo número inteiro: "))
    divi= n1/n2
   
except ValueError:
    print(f"Erro! Digite novamnete ")
except ZeroDivisionError:
    print(f"Erro! ao dividir por zero")
else:
    print(f"O programa não contém erro.")
    print(f"O resultado da divisão é {divi}")
finally:
    print(f"Fim do programa")