#INPUT
pi=3.14
radio=6

#PROCESSING
#Calculo del area de una esfera
area_de_la_esfera=(4*pi*radio**2)
a=(area_de_la_esfera<368)

#OUTPUT
print("el area de la esfera es igual o menor que 16", a)
