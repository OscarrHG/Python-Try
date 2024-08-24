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
print(f"Mi nombre es {name} {surname} y mi edad es {age}")