def somaImposto(taxaImposto, custo):

    imposto = custo * taxaImposto / 100

    custoFinal = custo + imposto

    return custoFinal

custo = float(input("Digite o custo: "))
taxa = float(input("Digite a taxa de imposto: "))

resultado = somaImposto(taxa, custo)

print("Valor final:", resultado)
