

def media_nota(nota1, nota2):
    media = (nota1 + nota2) / 2
    print("media das notas:", media)

def media_nota_retorno(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
def main():
    n1 = float(input("digite a primeira nota:"))
    n2 = float(input("digite a segunda nota:"))
    media = media_nota_retorno(n1, n2)
    print("media dentro do main:", media)
    
    if media >= 7:
        print("aprovado parabens:")
    else:
        print("reprovado")
main()
