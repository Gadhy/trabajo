#CALCULAR LA ENERGIA ELASTICA

#INPUT
K=float(input("ingrese K="))
x=float(input("ingrese x="))

#PROCESSING
energia_elastica=(K*(x**2))/2

#Verificacion
verificacion_de_la_energia_elastica=(energia_elastica==256)

#OUTPUT
print("la energia elastica es=" , energia_elastica)
print("la energia elastica es mayor que 236?", verificacion_de_la_energia_elastica)
