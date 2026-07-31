mes = int(input("Escribe el mes (1-12): "))
if 1 <= mes <= 12:
    match mes:
        case 12 | 1 | 2:
            estacion = "Invierno"
        case 3 | 4 | 5:
            estacion = "Primavera"
        case 6 | 7 | 8:
            estacion = "Verano"
        case 9 | 10 | 11:
            estacion = "Otoño"

    print("La estación es:", estacion)
else:
    print("Escribió un mes invalido...")