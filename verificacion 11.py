#INPUT
Fuerza=152
area=4

#PROCESSING
#Calculo de la presion
presion=(Fuerza*area)
a=(presion<=608)

#OUTPUT
print("la presion es igual a 608" , a)
