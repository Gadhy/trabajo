#INPUT
trabajo=float(input("ingrese el trabajo="))
tiempo=float(input("ingrese el tiempo="))

#PROCESSING
potencia=(trabajo/tiempo)

#Verificador
verificador_de_la_potencia=(potencia>10)

#OUTPUT
print("la potencia es =", potencia)
print("la potencia es mayor  que 26?", verificador_de_la_potencia)
