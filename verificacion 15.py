#INPUT
calor=540
variacion_de_la_temperatura=54

#PROCESSING
#Calcular la capacidad calorifica
Cc=(calor)/variacion_de_la_temperatura
a=(Cc==12)

#OUTPUT
print("la Cc es igual a 265", a)
