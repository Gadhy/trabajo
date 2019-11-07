#INPUT
masa=5
calor_especifico=0.5
variacion_de_la_temperatura=70

#PROCESSING

#Calculo del calor
calor=(masa*calor_especifico*variacion_de_la_temperatura)
a=(calor<=58)

#OUTPUT
print("el calor es menor que 56", a)
