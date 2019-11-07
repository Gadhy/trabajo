#Hallamos el promedio de un alumno

#INPUT
nota1=float(input("ingrese nota1="))
nota2=float(input("ingrese nota2="))
nota3=float(input("ingrese nota3="))

#PROCESSING
promedio=( nota1+nota2+nota3)/3

#VERIFICADOR
verificador_del_promedio=(promedio<26)

#OUTPUT
print("el promedio del alumno es", promedio )
print("el promedio es mayor que 26?", verificador_del_promedio)

