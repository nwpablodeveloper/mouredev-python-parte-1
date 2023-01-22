### CLASES ####


class MyEmptyPerson:
    pass 

print("=============================")
print(MyEmptyPerson)
print(MyEmptyPerson())
print("=============================")

print("\n")


class Person:
    def __init__(self, name, surname, alias ="Sin alias", inmodificable = "INMODIFICABLE"):
        self.__inmodificable = inmodificable # propiedad privada
        self.name = name
        self.surname = surname
        self.full_name = f"{ name } {surname} ** {alias} ** {inmodificable} "

    def walk (self):
        print(f"{ self.full_name } Está caminando")

    def get_inmodificable (self):
        return self.__inmodificable

#############################################
my_person = Person( "Romina", "Diaz")
print(f"{my_person.name} {my_person.surname} ")
print(my_person.full_name)
my_person.walk()
##############################################
    
print("\n")

##############################################
my_other_person = Person( "Pablo", "Veiga", "nwpablo", "inmodificable" )
my_other_person.name = "Romina"
my_other_person.__inmodificable ="MODIFICADO" ### IMPOSIBLE MODIFICAR DATO
print(my_other_person.name)
my_other_person.walk()
my_other_person.get_inmodificable()
##############################################
    
print("\n")