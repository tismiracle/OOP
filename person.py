

class Person:
    """name='' jest to to jak bysmy to definiowali w metodzie __init__
    last_name=''    jest to to jak bysmy to definiowali w metodzie __init__
    age=''  jest to to jak bysmy to definiowali w metodzie __init__"""
    
    raise_salary = 1.04

    def __init__(self, name, lastname, age, salary):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = name + "." + lastname + "@" + "nazwa.pl"
        self.salary = salary
        #super().__init__()

    def full_name(self):
        return f"{self.name} {self.lastname}"
    
    def count_salary(self):
        return self.salary * self.raise_salary

    @staticmethod
    def is_weekend(day):
        if day.weekday() == 6 or day.weekday() == 7:
            return True
        else:
            return False
    
    @classmethod
    def from_string(cls, person_string): #cls to potrzebne slowo i nie jest to wymyslone
        name, last_name, age, salary = person_string.split("_")
        return cls(name, last_name, age, salary)

    @property
    def additional_email(self):
        return "{}.{}@akademia.pl".format(self.name.lower(), self.lastname.lower())


person1 = Person("Zdzichu", "Python", 23, 400)
person2 = Person("Janek", "Java", 26, 600)
print(person1)
print(person2)

print(Person.full_name(person1)) #wyswietli zdzicha
print(Person.full_name(person2)) #wyswietl janka

print(person1.email)

print(person1.count_salary())

import datetime
print(Person.is_weekend(datetime.date(2020, 1, 14)))


person3 = Person.from_string("Agnieszka_Nowak_22_500")
#print(person3)
print(person3.full_name(), person3.age)

print(person3.additional_email)

#dziedziczenie, czyli budowa obiektu na bazie innego obiektu
#klasa ponizsza posiada swoje wlasciwosci ale ma dostep do wlasciwosci klasy nadrzednej
class Manager(Person):

    def __init__(self, name, lastname, age, salary, employees = None):
        super().__init__(name, lastname, age, salary) #dodaje wszystkie wartosci klasy Person
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


class Developer(Person):

    def __init__(self, name, lastname, age, salary, lang):
        super().__init__(name, lastname, age, salary)
        self.lang = lang

developer1 = Developer("Jan", "Kowalski", 23, 17000, "C++")
developer2 = Developer("Zygmunt", "Struś", 59, 7800, "Java")
manager1 = Manager("Ania", "Konieczna", 25, 9000, [developer1, developer2])

print(manager1.additional_email)

#polimorfizm
print(Person.full_name(manager1))
print(Developer.full_name(manager1))
print(Manager.full_name(manager1))
