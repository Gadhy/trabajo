#CALCULAR LA ENERGIA CINETICA

#INPUT
masa=float(input("ingrese la masa="))
velocidad=float(input("ingrese la velocidad="))

#PROCESSING
la_energia_cinetica=(masa*velocidad)/2

#Verificacion
verificacion_de_la_energia=(la_energia_cinetica==30)

#OUTPUT
print("la energia cinetica es=", la_energia_cinetica)
print("¿la energia cinetica es mayor que 26?", verificacion_de_la_energia)
