#CALCULAR EL VOLUMEN DEL CILINDRO
#INPUT
pi=float(input("ingrese pi="))
radio=float(input("ingrese el radio="))

#PROCESSING
el_volumen_de_un_cilindo=(pi*radio**2)

#VERIFICAR
verificar_el_volumen_del_cilindro=(el_volumen_de_un_cilindo==16)


#OUTPUT
print("el volumen del cilindro es" , el_volumen_de_un_cilindo)
print("el volumen es igual a 16?", verificar_el_volumen_del_cilindro)
