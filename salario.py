salario= int(input("Digite o valor do seu salario: "))

if salario >=5000:
    bonus = salario * 0.05
    valor_final = salario + bonus
    

elif salario >= 2000:
    bonus = salario * 0.10
    valor_final = salario + bonus
    
else:
        bonus= salario*0.05
        valor_final= salario+ bonus


print(f"Salário: R$ {salario}")
print(f"Valor do bônus: R$ {bonus}")
print(f"Salário final: R$ {valor_final}")