edad = int(input("ingrese su edad: "))
pais = input("ingrese su pais de origen: \nA: Austria \nCS: Corea del Sur \nC: Colombia \nG: Grecia \nS: Singapur\n").upper()

# 16 Austria 
# 19 corea
# 18 colombia
# 17 Grecia 
# 21 singapur 
if pais == "A" or  pais == "CS" or pais == "C" or  pais == "G" or pais == "S":
    if pais == "A" and edad >= 16:
        print ("Usted cumple la edad minima para votar en su pais de origen el cual es Austria") 
    elif pais == "CS" and edad >= 19:
        print ("Usted cumple la edad minima para votar en su pais de origen el cual es Corea del Sur")
    elif pais == "C" and edad >= 18:
        print ("Usted cumple la edad minima para votar en su pais de origen el cual es Colombia")
    elif pais == "G" and edad >= 17:
        print ("Usted cumple la edad minima para votar en su pais de origen el cual es Grecia ") 
    elif pais == "S" and edad >= 21:
        print ("Usted cumple la edad minima para votar en su pais de origen el cual es Singapur") 
    else:
        print ("su edad no cumple el estandar de su pais ")
else: 
    print ("Su pais no esta en el listado")

