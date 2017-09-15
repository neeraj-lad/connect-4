NUM_ROWS = 7
NUM_COLS = 6

import random

class Board:
	def __init__(self):
		# self.turn = 1 for first player(Blue), and -1 for second player(Red)
	
		self.turn = 1
		self.board = []
		self.last_move = []
	
		# Create an empty board
		for i in range(NUM_ROWS):
			self.board.append([0] * NUM_COLS)

	
	def generate_moves(self):
		available_moves = []
		
		for i in range(NUM_ROWS):
			for j in range(NUM_COLS):
				
				# If any column has an empty cell, then we can move to that column
				if self.board[i][j] == 0:
					available_moves.append(i)
					break
		
		return available_moves


	def make_move(self, move):
		inserted = False
		
		for j in range(NUM_COLS):

			# If column 'move' has an empty cell, then make move on that cell
			if self.board[move][j] == 0:
				self.board[move][j] = self.turn

				# Transfer turn to the other player
				self.turn *= -1
				
				self.last_move.append(move)
				inserted = True
				break

		if not inserted:
			print ("Cannot move to col %r, as it is already filled") % move
			return


	def unmake_last_move(self):
		# Initial state before any move
		if len(self.last_move) == 0:
			print ("Cannot unmove, as no move made yet")
			return 

		move = self.last_move.pop()
		deleted = False

		# Check for the last non-zero value inserted in the column 'move' & set it to zero
		for j in range(NUM_COLS-1, -1, -1):
			if self.board[move][j] != 0:
				self.board[move][j] = 0
				deleted = True

				# Rollback turn to the current player
				self.turn *= -1
				break

		if not deleted:
			print ("Cannot unmove from col %r, as it is already empty") % move
			return 


	def last_move_won(self):
		# For any player to win, atleast 7 moves need to be made on the board
		if len(self.last_move) < 7:
			return False

		# Check horizontal cells	
		for row in range(NUM_ROWS):
			count = 1
			for col in range(1, NUM_COLS):
				if self.board[row][col] != 0 and self.board[row][col] == self.board[row][col-1]:
					count += 1
					if count >= 4:
						return True
				else:
					count = 1

		# Check vertical cells
		for col in range(NUM_COLS):
			count = 1
			for row in range(1, NUM_ROWS):
				if self.board[row][col] != 0 and self.board[row][col] == self.board[row-1][col]:
					count += 1
					if count >= 4:
						return True
				else:
					count = 1
				

		# http://stackoverflow.com/questions/32770321/connect-4-check-for-a-win-algorithm
		
		# Check the lower diagonal from left edge to middle of board
		for i in range(3, NUM_COLS):
			row = 1
			col = i-1
			count = 1
			while row < NUM_ROWS and col > -1:
				if self.board[row][col] != 0 and self.board[row][col] == self.board[row-1][col+1]:
					count += 1
					if count >= 4:
						return True
				else:
					count = 1
				row += 1
				col -= 1

		# Check the upper diagonal from left edge to middle of board
		for i in range(1, 4):
			row = i+1
			col = 4
			count = 1
			while row < NUM_ROWS and col > -1:
				if self.board[row][col] != 0 and self.board[row][col] == self.board[row-1][col+1]:
					count += 1
					if count >= 4:
						return True
				else:
					count = 1
				row += 1
				col -= 1

		# Check the lower diagonal from right edge to middle of board
		for i in range(NUM_COLS-1, 2, -1):
			row = 5
			col = i-1
			count = 1
			while row > -1 and col > -1:
				if self.board[row][col] != 0 and self.board[row][col] == self.board[row+1][col+1]:
					count += 1
					if count >= 4:
						return True
				else:
					count = 1
				row -= 1
				col -= 1	

		# Check the lower diagonal from right edge to middle of board
		for i in range(NUM_ROWS-2, 2, -1):
			row = i-1
			col = 4
			count = 1
			while row > -1 and col > -1:
				if self.board[row][col] != 0 and self.board[row][col] == self.board[row+1][col+1]:
					count += 1
					if count >= 4:
						return True
				else:
					count = 1
				row -= 1
				col -= 1

		# There is no combination of 4 consecutive cells for either player, so last move did not win
		return False
	
	def __str__(self):
		s = "#" * 17
		s += "\n"
		for row in self.board:
			s += "# "
			for cell in row:
				if cell == -1:
					s += "R "
				elif cell == 1:
					s += "B "
				else:
					s += "  "
			s += "#\n"
		s += "#" * 17
		return s
