from random import randint
computador= randint(0,5) #Faz o computador "PENSAR"
print("Vou pensar em número entre 0 e 5. Tente advinhar...")
print('-=-'*10)

jogador= int(input("Em que número pensei: ")) # Jogador tenta advinhar
if jogador == computador:
    print("Parabéns! Você consegueiu me vencer")
else:
    print(f"Ganhei! Pensei no número {computador} e não no {jogador} ")