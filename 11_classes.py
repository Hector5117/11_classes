

#Classes

#Definicion

class MyEmptyPerson:
    pass #para poder dejar la clase vacia


print(MyEmptyPerson)
print(MyEmptyPerson())

#clase con constructor, funciones y propiedades privadas y publicas


class Person:
    def __init__(self, name, lastname, alias="Sin alias"):
        self.full_name = f"{name} {lastname} ({alias})" #propiedad publica
        self.__name = name #propiedad privada
        
    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} está caminando")
        
        

my_person = Person("Hector", "Sanchez")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Hector","Sanchez", "Laxer")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de leon (el loco de los gatos)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)