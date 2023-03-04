# Programa para saber si x es positivo y de 4 digitos

print("------------------------------------------")
print("------------Digite x----------------------")
print("------------------------------------------")

#input
x=int(input("Digite x: "))

#Procesing
if x > 0 :
    rta= "positivo "
else:
    rta = "negativo "
if (9999>x>1000) or (-1000>x>-9999):
    rt = "El numero tiene 4 digitos"
else: 
    rt = "El número no tiene 4 digitos"


#out
print("------------------------------------------")
print("---------Resultado__----------------------")
print("------------------------------------------")
print("El número x:" + str (rta))
print("El número x:" + str (rt))





