### FUNCTIONS ###


def my_function ( edad: int ):
    print("La edad es", edad)
    
my_function ( 34 )

########################################


def sum_two_values ( first_number: int, second_number: int ):
    print(first_number + second_number)

sum_two_values( 7, 34 )
sum_two_values( 10, 30)
###########################################

def sum_two_values_with_return( first_value, second_value ):
    return first_value + second_value

my_result = sum_two_values_with_return ( 15, 30 )
print(my_result)


def print_name ( name, surname ):
    print( f"{name} {surname}" )

print_name( surname = "Veiga", name = "Pablo")

###########################################

def print_name_with_dafault ( name , surname, alias = "Sin Alias" ):
    print(f"{ name } { surname } {alias} ")

print_name_with_dafault(surname="Dias", name="Romina", alias="rominawarrior")
print_name_with_dafault( "Sophia", "Veiga" )


###################################

def print_upper_texts (*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Holaf", "otra", "mas texto")