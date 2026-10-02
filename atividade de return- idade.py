def classificar_idade(idade):
    idade= 2026-ano

    if idade <12:
        return "É uma criança"
    elif idade > 13 and idade <=17:
        return "É um adolecente"
    elif 18 <= idade <= 59:
        return "É um adulto"
    else:
        return "É um idoso"
    



ano= int(input("digite o seu ano: "))
print(classificar_idade(ano))