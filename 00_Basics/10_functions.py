"""
Funciones
"""

def my_function ():
    print("Esto es una funcion")

my_function()

# Función con parámetros de entrada/argumentos
def sum_two_value(first_number, second_number):
    print(first_number + second_number)

sum_two_value(5, 7)
sum_two_value("6","9")
sum_two_value(2.1, 1.5)

# Función con parámetros de entrada/argumentos y retorno
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_value(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="HG", name="Oscar")

# Función con parámetros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios
def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")