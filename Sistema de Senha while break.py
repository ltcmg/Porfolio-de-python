tentativa = 0

while True:
    senha= int(input("Digite a sua senha: "))

    if senha == 1234:
         print(f"Acesso permitido!")
         break

    elif senha != 1234:
        print("senha incorreta")
        tentativa  += 1
        
    if tentativa ==3:
        print("Acesso negado")
        break

