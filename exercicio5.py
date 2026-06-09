def aprovado():
    print("Aprovado")

def recuperacao():
    print("Recuperacao")

def reprovado():
    print("Reprovado")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
n5 = float(input("Digite a quinta nota: "))

media = (n1 + n2 + n3 + n4 + n5) / 5

print("Media:", media)

if media >= 7:
    aprovado()
elif media >= 4:
    recuperacao()
else:
    reprovado()
