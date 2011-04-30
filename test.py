from CheckerBoard import CheckerBoard
from Point import Point
from GameState import GameState

class Checkers:
        
	#Fields
	#---------
	#checkersGui gui	The Gui Object "checkers.py"
	#Player white		The white player object
	#Player black		The black player object
	#Board b			The board object
	#int whiteScore		White's score (number of games won)
	#int blackScore		Black's score (number of games won)
	
	#Main sequence of operations.  Plays checkers until the user does not want to
	#
	#Use this class for testing your code. 
	#
	#There is some sample code here to see how to take input from a user on a command line (raw_input)
	#and how to call the functions you have implemented in another object. Note that we had to 
	#import the CheckerBoard class from the file called CheckerBoard. 
	#If you wanted to test the singleTurn method in Player.py, for instance, you would add to the top
	#of this file "from Player import Player". You would then add playerBlack = Player() and then
	#call playerBlack.singleTurn(). 
	
        def main(self):
                board = CheckerBoard()
                p_no = Point(1,7)
                p1 = Point(3,0)
                p2 = Point(2,3)
                p3 = Point(2,5)
                p4 = Point(1,4)
                p5 = Point(4,5)
                p6 = Point(5,4)
                p7 = Point(0,3)
                p8 = Point(1,7)
                game_state = GameState(GameState.WhitesTurn)
                print board.move(p_no,p1,game_state)
                print board.board[3][0]
                                
if __name__ == "__main__":
        checkers = Checkers()
        checkers.main()
