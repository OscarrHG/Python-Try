"""
Diccionarios
"""
my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Oscar",
                "Apellido": "HG", 
                "Edad": 21, 
                1: "Python"}
my_dict = {"Nombre": "Oscar",
            "Apellido": "HG", 
            "Edad": 21, 
            "Lenguajes": {"Python", "Swift", "Kotlin"},
            1: 1.75}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Jean"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Zapallal"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

# Búsqueda
print(my_dict[1])
print(my_dict["Nombre"])

print("Oscar" in my_dict)
print("Apellido" in my_dict)

# Otras operaciones
print("******************")
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Aleluya")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))