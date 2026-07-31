opcion = input("Ingrese nombre de artista, pelicula o serie: ").lower()
match opcion:
    case "interstellar":
        informacion = "Pelicula de ciencia ficcion dirigida por Christopher Nolan."
        print(informacion)
    case "queen":
        informacion = "Banda de rock britanica formada en 1970."
        print(informacion)
    case "breaking bad":
        informacion = "Serie de drama creada por Vince Gilligan."
        print(informacion)
    case "coco":
        informacion = "Pelicula animada de Pixar estrenada en 2017."
        print(informacion)
    case "taylor swift":
        informacion = "Cantautora estadounidense ganadora de multiples premios Grammy."
        print(informacion)
    case _:
        informacion = "No se encuentra con informacion al respecto..."
        print(informacion)