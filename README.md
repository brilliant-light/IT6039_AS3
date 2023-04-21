# IT6039_AS3
repository for software testing assignment

There were a lot of syntax errors in the initial document but they have now been corrected. 
This included things like naming conventions (changing to lowercase and using underscores), spacing between functions, spacing around mathematical symbols and more.

For example, one of the test cases had the same name as another test case. 
One of the test cases' names was spelled incorrectly (strike_score).

All 'self.game.rolls(x)' was changed to 'self.game.roll(x)' as the test cases had issues with referencing the list. 

In the game itself, the first scoring function was changed to check if it was a strike or not, this adjustment was hinted at by the 
original code already calling the strike function within it. 

Test cases the two extreme boundaries of the game; maximum and minimum number of points available. This is seen in the 'gutterball' and 'perfect game' test cases.
