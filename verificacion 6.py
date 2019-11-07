#INPUT
K=400
x=1.5

#PROCESSING
#Calculo
energia_elastica=(K*(x**2))/2
a=(energia_elastica==256)

#OUTPUT
print("la energia elastica es 156" , a)
