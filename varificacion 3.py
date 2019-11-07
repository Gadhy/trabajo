#INPUT
pi=3.14
radio=5

#PROCESSING

#calculo
el_volumen_de_un_cilindo=(pi*radio**2)
a=(el_volumen_de_un_cilindo<12)

#OUTPUT
print("el volumen del cilindro es menor que 12" , a)
