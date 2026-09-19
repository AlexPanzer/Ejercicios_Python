suma = 0
contador = 0


cantidad = int(input("Ingrese cantidad de numeros: "))
while (cantidad <= 0) :
    print("No sea pollo")
    cantidad =  int(input("Ingrese cantidad de numeros: "))     
    
if(cantidad>=1):
    numero = float(input("Ingrese un numero: "))
    suma += numero
    contador += 1
    cantidad = cantidad-1 
    
promedio = suma / contador
print("El contador es: ",contador," Promedio: ",promedio )