# DICCIONARIOS


my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = { 
                    "Nombre": "Pablo", 
                    "Apellido": "Veiga", 
                    "Edad": 34, 
                    1: "Python"
                }

my_dict = { 
            "Nombre": "Pablo", 
            "Apellido": "Veiga", 
            "Edad": 34, 
            "Lenguajes": {"Python", "Java", "Javascript"},
            6: 45662197
        }


print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Apellido"])

my_dict["Nombre"] = "Sophia"
print(my_dict["Nombre"])
print(my_dict[6])

# podemos agregar nuevas llaves al diccionario
my_dict["Calle"] = "Av. Paisos Catalans 2"
print(my_dict["Calle"])

# Eliminar elmentos ojo no elimina el DICT completo
del my_dict["Lenguajes"]
print(my_dict)

print("Apellido" in my_dict)
print("Veiga" in my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = [ "Nombre", 6, "Apellido", "Edad" ]

# crear un nuevo diccionario con nuevas llaves
my_new_dict = my_dict.fromkeys((my_list))
print(my_new_dict)

# Crear un nuvo diccionario vacio con las llaves iguales a otro
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)


# Creo con misma llaves que otro pero agrego valores por defecto
my_new_dict = dict.fromkeys(my_dict, "Pablo")
print(my_new_dict)

# Puedo transformar el tipo de dato
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))



print("\n \n")