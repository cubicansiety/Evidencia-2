precio=float(input("Escriba el precio del producto: "))
if precio<=100:
    descuento=0
elif precio<=200:
    descuento=0.1
elif precio<=500:
    descuento=0.2
else:
    descuento=0.25
print("El precio final seria: ", precio-(precio*descuento))