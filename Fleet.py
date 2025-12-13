class Fleet:
    def __init__(self, name):
        self.__name = name
        self.__spaceships = []

    def  append__spaceships (self , ship) :
       if len(self.__spaceships) < 15 :
           self.__spaceships.append(ship)
       else:
           print("you attended the maxmum of spaceships.")

    