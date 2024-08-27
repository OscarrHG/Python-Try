"""
Listas
"""

myList = list()     #Esto esa una lista
myOtherList = []    #Esto también es una lista

print(len(myList))

myList = [35, 24, 62, 52, 30, 30, 17]
print(myList)

myOtherList = [21, 1.75, "Oscar", "HG"]
print(myOtherList)

print(type(myOtherList))

print(myOtherList[0])
print(myOtherList[1])
print(myOtherList[-1])
print(myOtherList[-3:])
print(myOtherList[1:])
print(myOtherList[-3:])
print(myOtherList.count(30))
#print(myOtherList[4])  //IndexError
#print(myOtherList[-5]) //IndexError

print(myOtherList.index("HG"))

age, height, name, surname = myOtherList
print(name)

name, height, age, surname = myOtherList[2], myOtherList[1], myOtherList[0], myOtherList[3] 
print(name)

# Concatenacion de listas
print(myList + myOtherList)

# Queremos añadir un elemento
myOtherList.append("Aleluya")
print(myOtherList)

# Insertar eb un indice en especifico
myOtherList[1] = "Rojo"
print(myOtherList)

myOtherList.insert(1,"Rosado")
print(myOtherList)

# Eliminar de una lista
myOtherList.remove("Rosado")
print(myOtherList)
myList.remove(30)
print(myList)

print(myList.pop())  #Quita al ultimo elemento por defecto
print(myList)

myPopElement = myList.pop(2)
print(myPopElement)
print(myList)

del myList[2]
print(myList)

# Operaciones con listas

my_new_list = myList.copy()

myList.clear()
print(myList)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo
myList = "Hola Python"
print(myList)
print(type(myList))