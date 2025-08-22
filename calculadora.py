numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

opcioncalculadora = int(input("ingrese la operacion que desea realizar: 1 para sumar\n2 para restar\n3 para multiplicar\n4 para dividir\n5 para salir\n"))

if opcioncalculadora == 1:
    resultado = numero1 + numero2
    print("el resultado de la suma es:", resultado) 
elif opcioncalculadora == 2:
    resultado = numero1 - numero2
    print ("el resultado de la resta es:", resultado)
elif opcioncalculadora == 3:
    resultado = numero1 * numero2
    print ("el resultado de la multiplicacion es:", resultado)
elif opcioncalculadora == 4:
    resultado = numero1 / numero2
    if numero2 == 0:
        print ("error: no se puede dividir por 0")
    else:
        print ("el resultado de la division es:", resultado)
elif opcioncalculadora == 5: 
    print("saliendo de la calculadora")
else:
    print("opcion no valida, porfavor intente de nuevo")
