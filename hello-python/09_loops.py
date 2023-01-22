# Loops #

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condicion es >= 10")


while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print("Es igual a: ", my_condition)
        break

print("Mi condicion es menor que 20: -> ", my_condition)

# For
print("\n\n")
print("BUCLE FOR")

my_list = [ 7, 34, 34, 22, 4 ]

for element in my_list:
    print(element)


my_tuple = ( 7, 34, 34, "Sophi", "Romi", "Pablo" )
for element in my_tuple:
    print( "Tupla: ", element)


my_set = { "Pablo", "Andres", "Veiga" }
for element in my_set:
    print("Set: ", element)


my_dict = { "Nombre": "Pablo", "Apellido": "Veiga" }
for element in my_dict:
    print("Dic keys: ", element)

for element in my_dict.values():
    print("Dic valores: ", element)
else:
    print("El bucle for del diccionario ha terminado")
 


print("\n\n")


