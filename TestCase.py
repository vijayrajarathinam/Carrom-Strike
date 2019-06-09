from index import Game

'''

__name__  = Clean Strike

'''

class GameTestCases(Game):
    def __init__(self,):
        super(GameTestCases,self).__init__("Player 1", "Player 2")
        self.is_file = False
        self.outputHeader = [
            ["Player 1","Player 2",
             "Player 1 Points","Player 2 Points",
             "Total Coins","Total Black","Total Red"]
        ]

    # getter for input list
    @property
    def fileIO(self):
        return self.__fileIO

    # getter for input list
    @fileIO.setter
    def fileIO(self,name):
        self.__fileIO  = name

    @property
    def __eqIO(self):
        a, b = [], []
        try:
            for IO in range(len(self.fileIO)):
                a.append(self.fileIO[IO][0])
                b.append(self.fileIO[IO][1])
            return len(a) == len(b)
        except IndexError:
            print("scenario's for both player does not match please look into the input")
            return False

    #test cases starts running
    def run(self):
        lists = []
        if self.__eqIO:
            for testCase in self.fileIO:
                if self.fileIO.index(testCase) == 0: continue
                try:
                    print(testCase)
                    self.playChance(self.player1, pstrike=int(testCase[0]))
                    self.playChance(self.player2, pstrike=int(testCase[1]))
                    lists.append([testCase[0], testCase[1], self.player1.get_point,
                                  self.player2.get_point, self.get_all, self.get_black, self.get_red])
                    if self.mid_validation :break
                except ValueError as ve:
                    print(ve)
                    break
                except EnvironmentError as ee:
                    print(ee)
                    break
                except TypeError as te:
                    print(te)
                    break

                print("Player 1 scores = {p1} | Player 2 scores = {p2}".format(p1=self.player1.get_point,p2=self.player2.get_point))
                print("coins Remaining Black : {b} | Red : {r} | total : {t}".format(b=self.get_black, r=self.get_red,t=self.get_all))

            self.file(lists) if self.is_file else print(self.decide())

    #set value in file
    def file(self,lists):
        with open("output.csv", 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.outputHeader + lists + [['RESULT',self.decide(),'','','','','']])
            print("look into output.csv for result")

    #get value from file
    def get_file(self,file_name,per):
        with open(file_name, per) as csvFile:
            reader = csv.reader(csvFile)
            self.fileIO,self.is_file = [row for row in reader],True

if __name__ =="__main__":
    import sys,csv

    #init the GameTestCases
    testCase = GameTestCases()

    # try to fetch the file else except with pre define variables
    try:
        listarg = sys.argv
        arg1 = listarg[1]
        if arg1 is not None: testCase.get_file(arg1,"r")
    except IndexError:
        print("Match Inputs are taken from a variable(testCases) below")

        testCase.fileIO = [
            ["player 1","player 2"],
            [2, 2, ],[1, 3, ],
            [2, 2, ],[4, 6, ],
            [1, 1, ],[5, 1, ],
        ]

    # run the senarios to get output
    testCase.run()