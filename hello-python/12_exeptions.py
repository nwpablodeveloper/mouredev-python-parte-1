### EXEPTIONS Handling ### MANEJO DE ERRORES

print( "================" )
# GENERAMOS UN ERROR
number_one, number_two = 5, "string"
"""
# comprobar error a mano

if type(number_two) == int:
    print( number_one + number_two )
else:
    print("error")
"""
# try exept

try:
    print( number_one + number_two )
    print("No hay error")
except:
    print("Se produjo un error")


# try exept else
print( "==================" )

#number_two = 1

try:
    print(number_one + number_two)
except:
    print("Exploto el codigo")
else:
    # se ejecuta si entra por el try
    print("ELSE, se ejecuta si entra no hay error")
finally:
    # se ejecuta siempre con o sin entrar por el try
    print("FINALY, se ejecuta siempre entre o no por el try")


print( "================" )
print( "================" )

# captura de exepciones por tipo

try:
    print( number_one + number_two )
    print("No hay error")
except ValueError:
    print("ValueError")
except TypeError as error:
    print("TypeError", error)
except Exception as error:
    print("Error no se: ", error)



print( "================" )
print("\n")