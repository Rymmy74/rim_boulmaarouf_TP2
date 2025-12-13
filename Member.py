class Member : 

    def __init__(self, first_name, last_name, gender, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age

    def introduce_yourself(self):
        return f"Je m'apelle {self.__first_name} {self.__last_name} , je suis un(e) {self.__gender} de {self.__age} ."

 
    def _first_name(self):
        return self.__first_name


    def _first_name(self, value):
        self.__first_name = value

    def _last_name(self):
        return self.__last_name

    def _last_name(self, value):
        self.__last_name = value

    def _gender(self):
        return self.__gender

    def _gender(self, value):
        self.__gender = value

    def _age(self):
        return self.__age

    def _age(self, value):
        self.__age = value
