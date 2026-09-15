from time import sleep

def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=' ')
            cont += p
        print("FIM!")

    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=' ')
            cont -= p
        print("FIM!")


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)