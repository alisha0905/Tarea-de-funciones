def contar_vocales():
  palabra = input("Ingrese una palabra: ")
  vocales = "aeiouAEIOU"
  contador = 0
  for letra in palabra:
    if letra in vocales:
      contador += 1
  print("La palabra tiene " + str(contador) + " vocales")

contar_vocales()


def numeroprimos():
  numero= int(input("Dame un numero: "))
  if numero > 1:
    for i in range(2, numero):
      if numero % i == 0:
        print("El numero no es primo")
        break
    else:
      print("El numero es primo")

numeroprimos()
