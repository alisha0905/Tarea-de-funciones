#Conversión de Grados Celsius a Fahrenheit

def conversion():
  celcius= int(input("Grados Celcius: "))
  fahrenheit= (celcius * 9/5) + 32
  print("La temperatura en Fahrenheit es: " + str(fahrenheit))

conversion()