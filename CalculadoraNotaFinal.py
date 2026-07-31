nota_parcial=float(input("Notas parciales del 0 al 100: "))
nota_proyecto=float(input("Notas proyecto del 0 al 100: "))
nota_examen=float(input("Notas examen del 0 al 100: "))
if 0 <= nota_parcial <= 100 and 0 <= nota_proyecto <= 100 and 0 <= nota_examen <= 100:
    print("La nota final es: ",(nota_parcial*0.3)+(nota_proyecto*0.4)+(nota_examen*0.3) )
else:
    print("La/s nota/s deben ser menores o iguales a 100...")