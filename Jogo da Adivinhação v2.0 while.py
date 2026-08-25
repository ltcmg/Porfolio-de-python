from random import randint
computador= randint(0,10)
print (f"Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print(f"Será que você consegue advinhar qual foi? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(f"Mais.. Tente mais uma vez.")
        elif jogador > computador:
            print(f"Menos... Tente mais uma vez.")
print (f"Acertou com tantos palpites {palpites}. Parabéns !")
