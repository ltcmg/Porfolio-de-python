def reajusta_salario(salario, percentual):
  reajuste = salario * (percentual / 100)
  return salario + reajuste

# Programa Principal
salario = float(input("Informe seu salário atual: "))
percentual = float(input("Informe o percentual de reajuste: "))
novo_salario = reajusta_salario(salario, percentual)
print(f"Novo Salário: R$ {novo_salario}")