#Palindromo

def palidromo():
  palabra= input("Ingrese una palabra:")
  palabra= palabra.lower()
  palabra_invertida= palabra[::-1]
  if palabra == palabra_invertida:
    print("La palabra es palindromo")
  else:
    print("La palabra no es palindromo")

palidromo()

#Factorial

def factorial():
  numero = int(input("Ingrese un numero: "))
  factorial = 1
  for i in range(1, numero + 1):  
    factorial *= i
  print("El factorial es: " + str(factorial))

factorial()