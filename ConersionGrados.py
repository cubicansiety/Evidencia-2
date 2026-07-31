temperatura= float(input("Escribe la temperatura(grados Celsius): "))
opcion=int(input("Escribe a que medida quieres convertir(1=Fahrenheit, 2=Kelvin): "))
match opcion:
    case 1:
        resultado=(temperatura*9/5)+32
        print("La temperatura de Celsius a Fahrenheit es: ", resultado)
    case 2:
        resultado=temperatura+273.15
        print("La temperatura de Celsius a Kelvin es: ", resultado)
    case _:
        print("Escriba una opcion entre 1-2...")