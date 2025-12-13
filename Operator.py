from Member import Member
class Operator(Member):
    def __init__(self, first_name, last_name, gender, age ,role):
     super.__init__(self, first_name, last_name, gender, age)
     
     self.__role = role
     self.__experience = 0
    
    def act(self):
       return f"{self.__first_name} {self.__last_name} agit tant que {self.__role}."
    
    def gain_experience(self):
       self.__experience += 1


    def _role(self):
        return self.__role


    def _role(self, new_role):
        self.__role = new_role


    def _experience(self):
        return self.__experience

    def _experience(self, exp):
        if exp >= 0:
         self.__experience = exp
