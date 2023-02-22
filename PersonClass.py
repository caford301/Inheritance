
class Person:
    def __init__(self, n, a, t):
        self.__name = n
        self.__address = a
        self.__telephone = t

    def print_person(self):
        print(" Name: " + self.__name + "\n Address: " +
              self.__address + "\n Telephone" + self.__telephone)

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone


class Customer(Person):
    def __init__(self, n, a, t, cn, m):
        Person.__init__(self, n, a, t)
        self.__customer_number = n
        self.__mail = m

    def print_person(self):
        Person.print_person(self)
        # print("Customer Number: " + self.__customer_number +
        #     "\n Preference: " + self.__mail)
