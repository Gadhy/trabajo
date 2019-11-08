#INPUT
masa=int(input("ingrese la masa="))
calor_especifico=float(input("ingrese el calor especifico="))
variacion_de_la_temperatura=int(input("ingrese la variacion de la temperatura="))

#PROCESSING
calor=(masa*calor_especifico*variacion_de_la_temperatura)

#OUTPUT
print("##################################################################################")
print("##########  FORMULA DEL CALOR ####################################################")
print("##################################################################################")
print("############ masa:", masa , "#####################################################")
print("############ calor especifico", calor_especifico , "##############################")
print("############ variacion de la temperatura", variacion_de_la_temperatura , "########")
print("##################################################################################")
print("############### calor", calor , "#################################################")
print("##################################################################################")
