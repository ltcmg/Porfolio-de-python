salario = float(input("Informe o valor do seu salario:  "))
casa = float(input("Digite o valor da casa: "))
anos = int(input("digite os anos que gostaria de estar pagando a casa: "))

meses = anos * 12
prestacao = casa/ meses
limite = salario * 0.30

if prestacao < limite :
    print("Empréstimo aprovado")
elif prestacao == limite:
    print ("Empréstimo aprovado no limite máximo")
else:
    print("Empréstimo Negado!")