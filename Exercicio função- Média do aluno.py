def media(nota1, nota2, nota3):

    soma = (nota1 + nota2 + nota3) / 3

    print(f"A média é {soma}")

    if soma >=7:
        print("aprovado")
    elif soma >=5:
        print("Recuperação")
    else:
        print("Reprovado")

media(8, 7, 9)
