"""
Tuples
"""

#Definicion de una tipla
myTuple = tuple()
myOtherTuple = ()

myTuple = (21, 1.75, "Oscar", "HG", "Oscar")
myOtherTuple = (35, 60, 30)

print(myTuple)
print(type(myTuple))

print(myTuple[0])
print(myTuple[-1])
# print(myTuple[4])     //IndexError
# print(myTuple[-6])    //IndexError

print(myTuple.count("Oscar"))
print(myTuple.index("HG"))
print(myTuple.index("Oscar"))

#myTuple[1] = 1.80 TypeError: 'tuple' object does not support item assignment  

mySumTuple = myTuple + myOtherTuple
print(mySumTuple)

print(mySumTuple[-4:-1])

myTuple = list(myTuple)
print(type(myTuple))

myTuple[4] = "Aleluya"
myTuple.insert(1, "Rosado")
myTuple = tuple(myTuple)
print(myTuple)
print(type(myTuple))