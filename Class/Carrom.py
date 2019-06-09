import sys

class Carrom(object):
    def __init__(self):
        self.__black = 9
        self.__red = 1
        self.__all = self.__black + self.__red

    # getter for black carrom coins
    @property
    def get_black(self):
        return self.__black

    # setter for black carrom coins
    def set_black(self, x):
        self.__black = self.__black - x
        self.__all = self.__black + self.__red

    # getter for red carrom coins
    @property
    def get_red(self):
        return self.__red

    # setter for black carrom coins
    def set_red(self, y):
        self.__red -= y
        self.__all = self.__black + self.__red

    # getter for all carrom coins
    @property
    def get_all(self):
        return self.__black + self.__red

    # validation for every strike
    def validate(self,strike):
        self.set_black(1) if strike == 1 else self.set_black(0)
        if strike == 3 and self.get_red > 0:self.set_red(1)
        elif strike == 3 and self.get_red == 0: raise ValueError("Foul play Red can't be pocketed twice")
        elif strike in [1,2] and self.get_all == 0:  raise EnvironmentError("All coin are pocketed")





