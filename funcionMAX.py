#Máximo de Tres Números

def maximo():
  numeros = []
  i = 0
  while i < 3:
    numero = int(input(f"Dame el numero {i+1}: "))
    numeros.append(numero)
    i += 1
  print("El numero mayor es " + str(max(numeros)))

maximo()