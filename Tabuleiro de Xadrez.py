for linha in range(8):
    for coluna in range(8):
        if (linha + coluna) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()