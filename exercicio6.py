def menu():
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Mostrar saldo")
    print("4 - Sair")

def sacar(saldo):
    valor = float(input("Valor do saque: "))

    if valor <= saldo:
        saldo = saldo - valor
    else:
        print("Saldo insuficiente")

    return saldo

def depositar(saldo):
    valor = float(input("Valor do deposito: "))
    saldo = saldo + valor

    return saldo

def mostrarSaldo(saldo):
    print("Saldo:", saldo)

saldo = 0

while True:

    menu()

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        saldo = sacar(saldo)

    elif opcao == 2:
        saldo = depositar(saldo)

    elif opcao == 3:
        mostrarSaldo(saldo)

    elif opcao == 4:
        break
