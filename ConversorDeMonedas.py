cantidad=float(input("Escriba la cantidad en pesos mexicanos: "))
opcion=int(input("Escribe la moneda a convertir(1=USD, 2=EUR, 3=THB, 4=JPY, 5=KRW, 6=AUD, 7=PEN, 8=CAD, 9=VES, 10=ARS): "))
match opcion:
    case 1:
        conversion= cantidad/16.5
        print("El cambio es de: ", conversion,"USD")
    case 2:
        conversion= cantidad/18
        print("El cambio es de: ", conversion,"EUR")
    case 3:
        conversion= cantidad/0.45
        print("El cambio es de: ", conversion,"THB")
    case 4:
        conversion= cantidad/0.12
        print("El cambio es de: ", conversion,"JPY")
    case 5:
        conversion= cantidad/0.013
        print("El cambio es de: ", conversion,"KRW")
    case 6:
        conversion= cantidad/11.5
        print("El cambio es de: ", conversion,"AUD")
    case 7:
        conversion=cantidad/2.8
        print("El cambio es de: ", conversion,"PEN")
    case 8:
        conversion=cantidad/8.2
        print("El cambio es de: ", conversion,"CAD")
    case 9:
        conversion=cantidad/8.2
        print("El cambio es de: ", conversion,"VES")
    case 10:
        conversion=cantidad/0.0023
        print("El cambio es de: ",conversion,"ARS")
    case _:
        print("Escribio una opcion no valida...")