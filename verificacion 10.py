#HALLAR LA ACELERACION CENTRIPETA

#INPUT
Velocidad=float(input("ingrese la velocidad="))
radio=float(input(("ingrese el radio=")))

#PROCESSING
#Calculo de la aceleracion centripeta
Acp=(Velocidad**2)/radio

#Verificacion
verificacion_de_la_aceleracion_centripeta=(Acp==36)

#OUTPUT
print("la acerleracion centripeta es =", Acp)
print("la aceleeracion  entripeta es mayo que 12?", verificacion_de_la_aceleracion_centripeta)
