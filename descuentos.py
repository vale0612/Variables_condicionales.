precio = int(input("ingrese el precio del poducto que desea comprar : "))
tarjeta = input("tiene tarjeta de fidelidad: \nSI\nNO\n ").upper()

if tarjeta == "SI":
    if precio > 100000:
        descuento = 0.15
    elif 50000 <= precio <= 100000:
        descuento = 0.1
    elif 10000 <= precio < 50000:
        descuento= 0.05
    else: 
        descuento= 0

    valorTotal= precio - (precio * descuento)
    adicional = valorTotal - (valorTotal * 0.05)
    print ("el valor de su product con los descuentos es de", adicional)
elif tarjeta == "NO" :

    if precio > 100000:
        descuento = 0.15
    elif 50000 <= precio <= 100000:
        descuento = 0.1
    elif 10000 <= precio < 50000:
        descuento= 0.05
    else: 
        descuento= 0
    valorTotal= precio - (precio * descuento)
    print ("el valor total de su producto con el descuento es de: ", valorTotal)