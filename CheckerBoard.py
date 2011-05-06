from SquareState import SquareState
from Point import Point
from math import*

class CheckerBoard:
	board = []
	def __init__(self):
	#All initialization
		for col in range(8):
			self.board.append([])
			for row in range(8):
				if row < 3 and (col + row) % 2 == 1:
					self.board[col].append(SquareState.BLACK)
				elif row > 4 and (col + row) % 2 == 1:
					self.board[col].append(SquareState.WHITE)
				else:
					self.board[col].append(SquareState.EMPTY)
		

		
	"""
	This method is used for printing the board in ascii. It is only useful until the GUI is built.
	Remove for production
	"""     	
	def printBoard(self): 	
		result = "|---|---|---|---|---|---|---|---|\n"
		for row in range(len(self.board)): 	
			for col in range(len(self.board[0])):
				result += "|" + SquareState.printSquare(self.board[col][row],(row+col)%2==0)
			result +="|\n|---|---|---|---|---|---|---|---|\n"
		print result


	# Returns whether or not the game is over 
	def gameOver(self, game_state):
		return self.getAllMoves(game_state) == None
    	
	
	# Returns the colorInt of the winner (-1 if game not over)
	# Input is the color of the player who most recently had a turn
	def gameWinner(self, game_state):
		if game_state.get_state()== 5:
			return game_state.get_state
		else: return -1
	
	# Checks to see if the given move is legal.  
	# Inputs are two Point objects: the start point and the end point
	# Pre: 1)start and end are points in the 8*8 board 2)State is correct (either player is playing)
	def checkMove(self, start, end, game_state):
		if start.row%2 + start.column%2 != 1 or end.row%2 + end.column%2 !=1:
			return False
		if not (self.board[start.column][start.row]+1)//2 == game_state.get_state() or not self.board[end.column][end.row] == SquareState.EMPTY:
			return False
		if not end.row - start.row == abs(end.row - start.row)*(game_state.get_state()*2-3) and not self.board[start.column][start.row] == SquareState.WHITEKING and not self.board[start.column][start.row] == SquareState.BLACKKING:
			return False
		if abs(end.column - start.column) == 1 and abs(end.row - start.row) == 1 and not self.anyJump(game_state):
			return True
		return abs(end.column - start.column) == 2 and abs(end.row - start.row) == 2 and (self.board[(start.column + end.column)/2][(start.row + end.row)/2] == 5 - game_state.get_state()*2 or self.board[(start.column + end.column)/2][(start.row + end.row)/2] == 6 - game_state.get_state()*2)


	# Makes the given move.  Returns true if the player has another move, else false
	# Inputs are two point objects: the start point and the end point
	def move(self, start, end, game_state):
		self.board[end.column][end.row] = self.board[start.column][start.row]
		self.board[start.column][start.row] = SquareState.EMPTY
		if abs(start.row - end.row) == 2:
			self.board[(start.column+end.column)/2][(start.row+end.row)/2] = SquareState.EMPTY
		if end.row == 7 and game_state.get_state() == 2:
			self.board[end.column][end.row] = SquareState.BLACKKING
		elif end.row == 0 and game_state.get_state() == 1:
			self.board[end.column][end.row] = SquareState.WHITEKING
		step = 0
		#TODO: Shouldn't check for jumps unless the move just made was a jump
		if self.anyJump(game_state):
			return True
		return False
	
	# Returns a list of all available Points that can be moved to from Start
	# Input is a point object
	def getMoves(self,start,game_state):
		possibleMoves = []
		for step in range(8):
			x = int(start.column + (step//4+1)*cos(pi/4+pi/2*step)/abs(cos(pi/4+pi/2*step)))
			y = int(start.row + (step//4+1)*sin(pi/4+pi/2*step)/abs(sin(pi/4+pi/2*step)))
			if x <= 7 and x >= 0 and y <= 7 and y >= 0:
				end = Point(x,y)
				if self.checkMove(start,end,game_state):
					possibleMoves.append(end)
		return possibleMoves
	
	# Pre: Game state is BlacksTurn or WhitesTurn
	# Returns a list of all possible moves this player can make
	def getAllMoves(self, game_state):
		moves = []
		for column in range(len(self.board)):
			for row in range(len(self.board[column])):
				start = Point(col, row)
				availbleMoves = self.getMoves(start, game_state)
				if not not availbleMoves:
					for end in availbleMoves:
						moves.append([start,end])
		return moves
				
	# private function 
	# Return ture if there are any pieces that can jump
	def anyJump(self, game_state):
		for col in range(len(self.board)):
			for row in range(len(self.board[col])):
				start = Point(col, row)
				if self.canJumps(start, 0, game_state):
					return True
		return False
    
	# private function 	
	# Return true if user can any jump from a particular start
	def canJumps(self, start, step, game_state):
		if step == 4:
			return False
		if not (self.board[start.column][start.row]+1)//2 == game_state.get_state():
			return False
		x = int(start.column + 2*cos(pi/4+pi/2*step)/abs(cos(pi/4+pi/2*step)))
		y = int(start.row + 2*sin(pi/4+pi/2*step)/abs(sin(pi/4+pi/2*step)))
		if x <= 7 and x >= 0 and y <= 7 and y >= 0:
			if y - start.row == abs(y - start.row)*(game_state.get_state()*2-3) or self.board[start.column][start.row] == SquareState.WHITEKING or self.board[start.column][start.row] == SquareState.BLACKKING:
				if self.board[(start.column + x)/2][(start.row + y)/2] == 5 - game_state.get_state()*2 or self.board[(start.column + x)/2][(start.row + x)/2] == 6 - game_state.get_state()*2:
					if self.board[x][y] == SquareState.EMPTY and self.board[start.column][start.row] != SquareState.EMPTY:
						return True
		return True and self.canJumps(start, step+1,game_state)
