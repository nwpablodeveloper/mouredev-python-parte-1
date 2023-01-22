# ==== SETS =====

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = { "Pablo", "Veiga", 34 }
print(type(my_other_set))
print("longitud del set: ", len(my_other_set))

# un set no es una estructura ordenada
my_other_set.add("nwpablo")
print(my_other_set)

# no admite un valor repetido
my_other_set.add("nwpablo")
print(my_other_set)

# comprobar la existencia de un dato
print("Pablo" in my_other_set)
print("Pablito" in my_other_set)

# puedo remover a un elemnto
my_other_set.remove("nwpablo")
print(my_other_set)

# borro todo el contenido del set
my_other_set.clear()
print(my_other_set)
print("Longitud del set", len(my_other_set))

# Elimino el set por completo
del my_other_set
# print(my_other_set)

my_set = { "Sophia", "Veiga", 7 }
print(type(my_set))
my_list = list(my_set)
print(type(my_list))
print(my_list)

my_other_set = { "Python", "Java", "Angular" }

# puedo unir pero si hay info repetidos no los agrega
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_other_set).union({"hijab"}))

print(my_new_set.difference(my_set))

print("\n")