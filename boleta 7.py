#INPUT
cliente=input("cliente:")
cajero=input("cajero:")
kg_de_manzanas=int(input("ingresar los kg de manzana="))
precio_por_cada_kg_de_manzana=float(input("ingresar el precio por cada kg de manzana ="))

#PROCESSING
pago_total=(kg_de_manzanas*precio_por_cada_kg_de_manzana)


#OUTPUT
print("#############################################################################################")
print("################# BOLETA DE COMPRA ##########################################################")
print("########### cliente:" , cliente , "##########################################################")
print("########### cajero:" , cajero , "############################################################")
print("########### kd de manzanas", kg_de_manzanas , "##############################################")
print("########### precio por cada kg de manzana: s/.", precio_por_cada_kg_de_manzana, "############")
print("#############################################################################################")
print("###### pago total:", pago_total , "##########################################################")
print("#############################################################################################")
