#INPUT
cliente=input("cliente:")
cajero=input("cajero:")
pantalones=int(input("ingresar el numero de pantalones="))
precio_por_cada_pantalon=float(input("ingresar el precio de cada pantalon ="))

#PROCESSING
compra_total=(pantalones*precio_por_cada_pantalon)
IGV=(compra_total*0.18)
pago_total=(compra_total+IGV)

#OUTPUT
print("#############################################################################################")
print("################# BOLETA DE VENTA ###########################################################")
print("########### cliente:" , cliente , "##########################################################")
print("########### cajero:" , cajero , "############################################################")
print("########### pantalones", pantalones , "######################################################")
print("########### precio por cada pantalon: s/.", precio_por_cada_pantalon, "######################")
print("#############################################################################################")
print("###### compra total:", compra_total , "######################################################")
print("###### IGV:", IGV , "########################################################################")
print("#############################################################################################")
print("###### pago total:", pago_total , "##########################################################")
print("#############################################################################################")
