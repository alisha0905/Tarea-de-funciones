#Número Par o Impar


def numeroparoimpar():
  numero=int(input("Ingrese un número para saber si es par o impar: "))
  if numero % 2 == 0:
    print("El numero es par")
  else:
    print("El numero es impar")

numeroparoimpar()