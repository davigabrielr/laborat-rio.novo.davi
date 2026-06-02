vetorA = []

while len(vetorA) < 10:
    num = int(input("Digite um valor: "))

    if num not in vetorA:
        vetorA.append(num)
    else:
        print("Valor já digitado!")

vetorB = []

for i in range(9, -1, -1):
    vetorB.append(vetorA[i])

print("\nVetor A:", vetorA)
print("Vetor B:", vetorB)
