print("Conversor de temperatura")
valor = float(input("Ingrese el valor de la temperatura: "))
origen = input("Ingrese la escala origen (C, F, K): ").upper()
destino = input("Ingrese la escala destino (C, F, K): ").upper()
salida = 0
temp_c =0 

if origen == "C":
        temp_c = valor
elif origen == "F":
        temp_c = (valor - 32) * 5 / 9
elif origen == "K":
        temp_c = valor - 273.15
else:
    print("Escala origen no válida.")

if destino == "C":
        salida=  temp_c
elif destino == "F":
        salida=  temp_c * 9 / 5 + 32
elif destino == "K":
        salida=  temp_c + 273.15
else:
        print("Escala destino no válida.")

print (salida)
