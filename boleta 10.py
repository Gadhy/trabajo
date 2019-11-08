#INPUT
cliente=input("cliente:")
cajero=input("cajero:")
metros_de_tela=int(input("ingresar los metros de tela="))
precio_por_cada_metro_de_tela=float(input("ingresar el precio por cada metro de tela ="))

#PROCESSING
pago_total=(metros_de_tela*precio_por_cada_metro_de_tela)

#OUTPUT
print("#######################################################################################################")
print("################# BOLETA DE PAGO ######################################################################")
print("########### cliente:" , cliente , "####################################################################")
print("########### cajero:" , cajero , "######################################################################")
print("########### metros de tela", metros_de_tela , "########################################################")
print("########### precio por cada metro de tela: s/.", precio_por_cada_metro_de_tela, "######################")
print("#######################################################################################################")
print("###### pago total:", pago_total , "####################################################################")
print("#######################################################################################################")
