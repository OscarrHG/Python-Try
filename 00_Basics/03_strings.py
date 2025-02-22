"""
Strings
"""

myString = "Mi string"
myOtherString = 'Mi otro string'

print(len(myString))
print(len(myOtherString))

print(myString + "---" + myOtherString)

myNewLineString = "Este es un String\ncon salto de linea"
print(myNewLineString)

myTabString = "\tEste es un String con tabulacion"
print(myTabString)

myScapeString = "\\tEste es un string \\nescapado"
print(myScapeString)

#Formateo
name, surname, age = "Oscar", "HG", 21
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #No recomendado
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #Inferencia de datos

# Desempaquetanto Caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(f)


# Division
languageSlice = language[1:3]
print(languageSlice)
languageSlice = language[1]
print(languageSlice)
languageSlice = language[-2]
print(languageSlice)

# Reverse
reversed_language =  language[::-1]
print(reversed_language)

# Funciones (Sistema)
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo