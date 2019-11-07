#INPUT
intensidad_de_corriente_electrica=1.5
resistencia=8

#PROCESSING
#calculo del voltaje
Voltaje=(intensidad_de_corriente_electrica*resistencia)
a=(Voltaje<9)

#OUTPUT
print("el voltaje es mayor que 15", a)
