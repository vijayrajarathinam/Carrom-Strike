from Class.Carrom import Carrom
from Class.Player import Player

'''
Game is the output of entire gsame played senarios 
'''

class Game(Carrom, Player):
    def __init__(self,player1,player2):
        super().__init__()
        self.player1 = self.get_player(name = player1)
        self.player2 = self.get_player(name = player2)
        self.loop = True

    # check who wins or draw
    def decide(self):
        if self.case1() is not None: return self.case1()
        if self.case2() is not None: return self.case2()
        if self.case3() is not None: return self.case3()

    # scenario for Player 1 to win
    def case1(self):
        return self.chance(self.player1,self.player2)

    # scenario for Player 2 to win
    def case2(self):
        return self.chance(self.player2,self.player1)

    # scenario for Both Players to have same value
    def case3(self):
        if self.player2.__eq__(self.player1): return "Match is draw"

    #strike the coin and validation for every player
    def playChance(self,playobj,pstrike=None):
        self.validate(pstrike)
        playobj.attempt(pstrike)

    @property
    def mid_validation(self):
        print(abs(self.player1.get_point-self.player2.get_point))
        return True if (abs(self.player1.get_point-self.player2.get_point) >= 5) \
                       and (self.player1.get_point >=5 or self.player2.get_point >=5) else False

    # player validation
    def chance(self, plr1, plr2):
        match, p = "draw", False
        if plr1.__gt__(plr2):
            if plr2.get_point in range(plr1.get_point - 2, plr1.get_point): p = True
            if plr1.get_point > 4 and not p: match = "{} Wins".format(plr1.name)
        else:
            return None
        return match

