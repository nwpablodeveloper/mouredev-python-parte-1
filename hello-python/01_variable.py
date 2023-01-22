# Variables

my_string_variable = 'My String variabless'
print( my_string_variable )

my_int_variable = 7
print( my_int_variable )

my_int_to_str_variable = str( my_int_variable )
print( my_int_to_str_variable )
print( type( my_int_to_str_variable ) )

my_bool_variable = False
print( my_bool_variable )

# Concatenación de variables en un print 
print( my_string_variable, my_int_variable, my_bool_variable )

# Fucinoes precargadas en el sistema
print( len( my_string_variable ) )


# Variables en una sola linea
name, surname, alias, age = "Pablo", "Veiga", "nwpablo", 34
print( name, surname, alias, age )

name = input( "Cuál es tu nombre ?" )
age = input( "Cuántos años tienes?" )

print( name )
print( age )

variable_cambia_tipo: str = "En Python la variable cambia el tipado"
variable_cambia_tipo = 34
variable_cambia_tipo = True
variable_cambia_tipo = 7.8
print( type( variable_cambia_tipo ) )