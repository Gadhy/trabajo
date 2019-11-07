#Hallar el trabajo

#INPUT
fuerza=float(input("ingrese la fuerza="))
distancia=float(input("ingrese la distancia="))

#PROCESSING
trabajo=(fuerza*distancia)

#Verificador
verificador_del_trabajo=(trabajo<=15)

#OUTPUT
print("¿el trabajo es?=", trabajo)
print("el trabajo es mayor o igual que 37", verificador_del_trabajo)
