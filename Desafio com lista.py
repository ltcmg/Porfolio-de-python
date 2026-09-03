numeros= []
numero= int(input("Digite um numero:"))
numeros.append(numero)

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    
print(f"Lista: {numeros}")
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
print(f"Soma: {sum(numeros)}")
print(f"Quantidade: {len(numeros)}")

