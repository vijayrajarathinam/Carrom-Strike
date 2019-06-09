
class Player():
    def __init__(self,**kwargs):
        self.name = kwargs.get("name")
        #lambda to all scenarios for possiblities of a player pocketing a coin
        self.scenarios = {
            1: lambda : self.Strike(),
            2: lambda : self.Multi_Strike(),
            3: lambda : self.Red_Strike(),
            4: lambda : self.Striker_Strike(),
            5: lambda : self.Defunct_Coin(),
            6: lambda :self.Not_Pocketed(),
        }
        self.__points =  0
        self.__attempt = 0
        self.__foul = 0

    # returns an instance of the class
    def get_player(self, name):
        return Player(name=name)

    # dunder gt : magic method for value greater than comparision value
    def __gt__(self, other):
        return self.get_point > other.get_point

    # dunder eq : magic method for value equal than comparision value
    def __eq__(self, other):
        return self.get_point == other.get_point

    #getter for number of player's attempts
    @property
    def get_attempt(self):
        return self.__attempt

    #setter for number of player's attempts
    def set_attempt(self,att):
        self.__attempt +=att

    #getter for player points
    @property
    def get_point(self):
        return self.__points

    #setter for player points
    def set_point(self, x):
        self.__points = x

    # getter for player's foul
    def set_foul(self, fou):
        self.__foul += fou

    #add points to player
    def __add(self, new):
        self.__attempt = 0
        self.__points += new

    #sub points to player
    def __sub(self, new):
        if(self.__foul > 2):
            self.__points -= 2
        elif(self.__foul > 0):
            self.__points -= 1
        self.__points -= new

    #player scenario to hit strike
    def Strike(self):
        self.__foul = 0
        return self.__add(1)

    # player scenario to hit multi-strike
    def Multi_Strike(self):
        self.__foul = 0
        return self.__add(2)

    # player scenario to hit Red strike
    def Red_Strike(self):
        self.__foul = 0
        return self.__add(3)

    # player scenario to hit striker
    def Striker_Strike(self):
        self.set_foul(1)
        return self.__sub(0)

    #player scenario to hit the coin out of the board
    def Defunct_Coin(self):
        self.set_foul(1)
        return self.__sub(1)

    # player scenario to miss the coin
    def Not_Pocketed(self):
        self.set_attempt(1)
        if self.get_attempt > 2: self.__sub(1)

    #player scenario
    def attempt(self,_key):
        if _key in range(1,7):
            func = self.scenarios.get(_key,None)
            return func()
        else:
            raise TypeError("input consist of invalid digit of scenario so this chance has been skipped. please give an number from 1 to 6")




