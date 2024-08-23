# Declaracion de Variables

myStringVariable = "my String variable"
print(myStringVariable)

myIntVariable = 5
print(myIntVariable)

myIntToStrVariable = str(myIntVariable)
print(myIntToStrVariable)
print(type(myIntToStrVariable))

myBoolVariable = False
print(myBoolVariable)

# Concatenacion de variables en un print
print("Hola, Oscar")
print("Hola,","Oscar", myIntToStrVariable, myBoolVariable)
print(len("Hola, Oscar"))
print(type(print("Mi cadena de texto"))) # Tipo 'NoneType'
print("Este es el valor de mi bool:", myBoolVariable)

# Algunas funciones del sistema (Python)
print(len(myIntToStrVariable))
print(len(myStringVariable))

# Variables en una sola linea ¡NO ABUSAR DE ESTA SINTAXIS!
name, surname, alias, age = "Oscar", "HG", "ArzenDev", 21
print("Me llamo:",name, surname, ". Mi edad es:", age, "Y mi alias es:", alias)

"""
first_name = input('Mi nombre es: ')
age = input('Mi edad es: ')

print(first_name)
print(age)
"""

# Cambiamos el tipo de variables
first_name = 45
age = "Pepe"

print(first_name)
print(age)

# Fozamos el tipo de variable? , quizas en los imput tendria mas sentido
address: str = "Mi direccion"
address = True
address = 5
address = 1.3
print(type(address))