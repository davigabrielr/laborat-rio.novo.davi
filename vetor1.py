#sor eu faltei dai tive que pesquisar como fazer

vetor = []
qtd_maior_30 = 0
soma_maior_30 = 0
soma_total = 0

for i in range(8):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

    soma_total += num

    if num > 30:
        qtd_maior_30 += 1
        soma_maior_30 += num

print("\nValores do vetor:")
for num in vetor:
    print(num)

print("\nQuantidade de números maiores que 30:", qtd_maior_30)
print("Soma dos números maiores que 30:", soma_maior_30)
print("Soma de todos os números:", soma_total)
