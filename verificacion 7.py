#CALCULA LA FUERZA

#INPUT
masa=float(input("ingrese masa="))
aceleracion=float(input("ingrese aceleracion="))

#PROCESSING
fuerza=(masa*aceleracion)

#Verificador
verificar_la_fuerza=(fuerza<=24)

#OUTPUT
print("la fuerza es =", fuerza)
print("la fuerza es mayor que 12?", verificar_la_fuerza)
