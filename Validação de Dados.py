sexo= str(input("Informe o seu Sexo, por favor :  [M/F]")).strip().upper()[0]
while sexo not in "MF":
    sexo= str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"O {sexo} registrado com sucesso")