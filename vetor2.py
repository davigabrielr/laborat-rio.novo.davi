vetor = []

while len(vetor) < 10:
    num = int(input("Digite um valor: "))

    if num not in vetor:
        vetor.append(num)
    else:
        print("Valor já digitado!")

maiores_100 = []

for num in vetor:
    if num > 100:
        maiores_100.append(num)

print("\nQuantidade de valores maiores que 100:", len(maiores_100))
print("Valores maiores que 100:")

for num in maiores_100:
    print(num)
