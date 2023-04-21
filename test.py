import unittest #imports the testing framework
import BowlingGame #imports the class for the bowling game

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame.BowlingGame() #sets up an instance of the test


    # test cases for one type of roll 

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0,16)
        assert self.game.score() == 24

    # test for one strike


    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(0,17)
        assert self.game.score() == 16

    # test for one spare


    def test_gutter_game(self):
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score() == 0

    # test for a gutter game AKA no pins knocked down

    def test_all_ones(self):
        self.roll_many(1,20)
        assert self.game.score() == 20

    # test for only knocking one pin down each turn

    def test_all_fours(self):
        self.roll_many(4,20)
        assert self.game.score() == 80

    # test for only knocking four pins down each turn

    def test_all_five(self):
        self.roll_many(5,20)
        assert self.game.score() == 100

    # test for only knocking four pins down each turn


    def test_perfect_game(self):
        self.roll_many(10,12)
        assert self.game.score() == 300

    # testing for the 'perfect game'

    def test_many_spare(self):
        self.roll_many(5,21)
        assert self.game.score() == 150

    # testing for many spares

    def roll_many(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main() 

# the above runs the test cases

