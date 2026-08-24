c= 0
n = int(input("Digite um número: "))
while n != 0:
    if n > 0:
        c = c + 1

    n = int(input("Digite outro número: "))

print(f"Você digitou {c} números positivos.")