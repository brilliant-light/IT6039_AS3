#File 2 (BowlingGame.py)
#This file has information about Bowling Game

class BowlingGame:
    def __init__(self):
        self.rolls = []

    # initialised a new list for each game



    def roll(self, pins):
        self.rolls.append(pins)

    # adds the number of pins


    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):

            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1

            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2

            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result
        
    # runs the game and checks to update the score at each frame

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    
    # checks if the current score is a strike

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
    
    # checks if the current score is a spare
    # (current roll + next roll adds to 10 or not)

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]
    
    # calculates score including bonus points after a strike

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    # calculates score including bonus points after a spare

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
    
    # calculates frame when neither strike or spare was achieved