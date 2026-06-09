def calcularCompra(quantidade):

    if quantidade <= 12:
        total = quantidade * 0.40
    else:
        total = quantidade * 0.25

    return total

quantidade = int(input("Digite a quantidade de laranjas: "))

valor = calcularCompra(quantidade)

print("Valor total da compra:", valor)
