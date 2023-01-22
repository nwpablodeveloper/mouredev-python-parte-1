### Strings

my_string = "Mi String"
my_other_string = 'Mi String'

print( len( my_string ) )
print( len( my_other_string ) )

print( my_string + " " + my_other_string )

my_new_line_string = "Este es un Strong \ncon salto de linea"
print( my_new_line_string )

my_tab_string = "\tMi estring esta tabulado"
print( my_tab_string )

my_scape_string = "\\t Mi estring esta tabulado \\n escapo"
print( my_scape_string )


### FORMATEO

print( "=======FORMATEO===========" )

name, surname, age = "Pablo", "Veiga", 34   

print( "Mi nombre es: {} {} y mi edad es {} ".format( name, surname, age ) )
print( "Mi nombre es: %s %s y mi edad es %d" %( name, surname, age ) )
print( f"Mi nombre es { name } { surname } y mi edad es { age } " )


## Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print( a )
print( b )
print( c )
print( d )
print( e )
print( f )


# Division
language_slice = language[ 1:6 ]
print( language_slice )


# Reerse
reverse_language = language[ ::-1 ]
print( reverse_language )

# Funciones
print( "1", language.upper() )
print( "2", language.capitalize() )
print( "3",  language.count('t')  )
print( "4", language.isnumeric() )
print( "5", language.lower() )
print( "6", language.upper().isupper() )
print( "7", language.lower() )
print( "8", language.startswith("Py") )
