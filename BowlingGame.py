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
        roll_index = 0
        for frameIndex in range(10):

            if self.is_strike(roll_index):
                result += self.strike_score(roll_index)
                roll_index += 1

            elif self.is_spare(roll_index):
                result += self.spare_score(roll_index)
                roll_index += 2

            else:
                result += self.frame_score(roll_index)
                roll_index += 2
        return result
        
    # runs the game and checks to update the score at each frame

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10
    
    # checks if the current score is a strike

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
    
    # checks if the current score is a spare
    # (current roll + next roll adds to 10 or not)

    def strike_score(self, roll_index):
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
    
    # calculates score including bonus points after a strike

    def spare_score(self, roll_index):
        return 10 + self.rolls[roll_index + 2]

    # calculates score including bonus points after a spare

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
    
    # calculates frame when neither strike or spare was achieved