#CALCULAR EL AREA DEL CILINDRO

"INPUT"
pi=float(input("ingrese pi="))
radio=float(input("ingrese el radio="))
generatriz=float(input("ingrese la generatriz="))


#PROCESSING
area_del_cilindo=(2*pi*radio*generatriz)

#VERIFICACION
verificar_el_area_del_cilindro=(area_del_cilindo<36)


#OUTPUT
print("el area del cilindro es", area_del_cilindo)
print("el area del cilindro es igual a 16?", verificar_el_area_del_cilindro)
