vetor = []

while len(vetor) < 10:
    num = int(input("Digite um valor: "))

    if num not in vetor:
        vetor.append(num)
    else:
        print("Valor já digitado!")

print("\nValores pares e suas posições:")

for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        print(f"Posição {i}: {vetor[i]}")
