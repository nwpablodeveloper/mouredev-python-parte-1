# =============================
# ======TUPLAS================
# =============================

print("======TUPLAS Es un conjunto de valores========\n")
print("======no puedo modificar los datos cargados========\n")


my_tuple = tuple()
my_other_tuple = ( 7, "Sophia", "Veiga")

my_tuple = ( 34, 1.72, "Pablo", "Pablo", "Veiga" )
print( my_tuple )
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) indexError
# print(my_tuple[-6]) indexError


print(my_tuple.count("Pablo"))
print(my_tuple.index("Veiga"))
print(my_tuple.index("Pablo"))

# my_tuple[1] = 1.70  # No puedo modificar
print( my_tuple )

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:5])

print("===CAMBIAR DE TUPLA A LISTA====\n \n")

print(type(my_tuple))
my_tuple = list(my_tuple)
print(type(my_tuple))

# ahora si se pueden cambiar valores

print(my_tuple)
my_tuple[3] = "Andrés"
my_tuple.insert(3, "Azul")
print(my_tuple)

""" y aca vuelvo a comvertirla en tupla asi las datos 
no se pueden modificar """

my_tuple = tuple(my_tuple)
print(type(my_tuple))

# del my_tuple # borro la tupla
#print(my_tuple)



print("\n ")




