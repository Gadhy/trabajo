#INPUT
apotema=6
semiperimetro=8

#PROCESSING
#Calculo del area lateral de una piramide
area_lateral=(semiperimetro*apotema)
a=(area_lateral<23)

#OUTPUT
print("el areal lateral de la piramide es menor que 36", a)
