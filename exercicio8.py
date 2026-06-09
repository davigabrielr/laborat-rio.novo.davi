def converterHora(hora, minuto):

    if hora == 0:
        print("12:", minuto, "A.M.")

    elif hora < 12:
        print(hora, ":", minuto, "A.M.")

    elif hora == 12:
        print(hora, ":", minuto, "P.M.")

    else:
        print(hora - 12, ":", minuto, "P.M.")

hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))

converterHora(hora, minuto)
