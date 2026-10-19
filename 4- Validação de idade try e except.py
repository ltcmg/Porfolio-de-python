try:
    idade= int(input("Informe a sua idade: "))
except ValueError:
    print("Erro! Digite uma idade válida usando números inteiros.")

if idade < 0:
        print("Erro! A idade não pode ser negativa.")

elif idade <18:
    print("Menor de idade")
else:
    print("Maior de idade")
