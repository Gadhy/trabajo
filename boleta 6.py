#INPUT
alumno=input("alumno:")
tesorera=input("tesorera:")
cursos=int(input("ingresar el numero de cursos="))
precio_por_cada_curso=int(input("ingresar el precio de cada curso="))

#PROCESSING
pago_total=(cursos*precio_por_cada_curso)

#OUTPUT
print("#####################################################################################")
print("################# BOLETA DE PAGO ####################################################")
print("########### alumno:" , alumno , "####################################################")
print("########### tesorera:" , tesorera , "################################################")
print("########### cursos", cursos , "######################################################")
print("########### precio por cada curso: s/.", precio_por_cada_curso, "####################")
print("#####################################################################################")
print("###### pago total:", pago_total , "##################################################")
print("#####################################################################################")
