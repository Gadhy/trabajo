#CALCULO DE LA ENERGIA POTENCIAL

#INPUT
masa=float(input("ingrese la masa="))
gravedad=float(input("ingrese la gravedad="))
altura=float(input("ingrese la altura="))

#PROCESSING
Energia_potencial=(masa*gravedad*altura)

#Verificacion
verificacion_de_la_energia_potencial=(Energia_potencial<=32)

#OUTPUT
print("la energia potencial es=" , Energia_potencial)
print("¿la energia potencial es igual a 78?", verificacion_de_la_energia_potencial)

