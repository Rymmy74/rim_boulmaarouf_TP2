from Member import Member

class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age):
       super.__init__(self, first_name, last_name, gender, age)

       self.__mana = 100

    def act(self , operator):
       if self.__mana >= 20:
            self.__mana -= 20
            return f"{self.get_first_name()} influence {operator.get_first_name()} {operator.get_last_name()} : {operator.act()}"
       else:
         return f"{self.get_first_name()} n'a pas assez de mana."
       
    def recharge_mana(self):
       self.mana = min(100, self.mana + 50)

  

    def _mana(self):
        return self.__mana

  
    def _mana(self, new_mana):
      if 0 <= new_mana <= 100:
        self.__mana = new_mana

