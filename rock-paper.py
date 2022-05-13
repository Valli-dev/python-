class Participant:
    def __init__(self, name):
        self.name= name
        self.points=0
        self.choice=""

    def choose(self):
        self.choice= input("Enter your choice {name}: Rock, Paper, Scissor?".format(name=self.name))
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))

    def toNumericalChoice(self):
        switcher = { "rock": 0, 
                     "paper":1, 
                     "scissor": 2
                    }
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):

        self.rules =[
            [0,-1,1],
            [1,0,-1],
            [-1,1,0]
        ]
        p1.choose()
        p2.choose()
        result= self.compareChoices(p1,p2)
        print("Round resulted in {result}".format(result = self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
            
    def compareChoices(self, p1, p2):
        #print("implemet")
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    
    def getResultAsString(self, result):
        res = { 0 : "draw", 1 : "win", -1: "loss"}
        return res[result]
    def awardPoints(self):
        print("implement")

class Game:
    def __init__(self):
        self.endGame=False
        self.participant = Participant( "Sam")
        self.secondParticipant = Participant( "Ram")

        
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()


    def checkEndCondition(self):
        #print("implement")
        answer = input("Continue Game? y/n :")
        if answer =="y":
            gameround = GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("GameEnded, {p1name} has {p1points} and {p2name} has {p2points} ".format(p1name=self.participant.name, p1points=self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True


    def determineWinner(self):
        #print("implement")
        resultString="It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name= self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name= self.secondParticipant.name)
        print(resultString)





game = Game()
game.start()