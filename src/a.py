import random
import board
import time

NUM_ROWS = board.NUM_ROWS
NUM_COLS = board.NUM_COLS

class Player:
    def __init__(self):
        self.board = board.Board()
        pass

        def name(self):
            return 'N'

        def make_move(self, move):
            inserted = False
                for j in range(board.NUM_COLS):
                    if self.board.board[move][j] == 0: 
                        self.board.board[move][j] = self.board.turn

                                # Transfer turn to the other player
                                self.board.turn *= -1

                                self.board.last_move.append(move)
                                inserted = True
                                break

                if not inserted:
                    print ("Cannot move to col %r, as it is already filled") % move
                        return

        def get_move(self):
            value, next_move = self.alpha_beta_negamax_root(self.board, 6, float('-inf'), float('inf'))
                if next_move is None:
                    return random.choice(self.board.generate_moves())
                return next_move

        def alpha_beta_negamax_root(self, board, depth, alpha, beta):
            #print (("Depth: %r") % (8 - depth))
                #print (board)
                if board.last_move_won():
                    # print ("-" * 50)
                        # print (("Found win for: %r") % (board.turn))
                        return board.turn * float('inf'), None
                if depth == 0:
                    e = self.eval(board)
                        return e, None
                next_move = None
                available_moves = board.generate_moves()
                for move in available_moves:
                    board.make_move(move)
                        v, nm = self.alpha_beta_negamax_root(board, depth-1, -beta, -alpha)
                        v *= -1
                        board.unmake_last_move()
                        if v >= beta:
                            return beta, move
                        elif v > alpha:
                            alpha = v
                                next_move = move
                #print (("Returning val, move: [%r, %r] from depth: %r") % (alpha, next_move, 8 - depth))
                return alpha, next_move	


        # Heuristic source: https://github.com/erikackermann/Connect-Four
        # H(n) = (my_fours * 1000 + my_threes * 100 + my_twos) - (oppo_fours * 1000 + oppo_threes * 100 + oppo_twos)
        # Where, my_fours = 4 consecutive cells of current player, and so on
        def eval(self, board):
            oppo = board.turn * -1

                my_fours = 0
                my_threes = 0
                my_twos = 0
                oppo_fours = 0
                oppo_threes = 0
                oppo_twos = 0

                # Check horizontal cells	
                for row in range(NUM_ROWS):
                    count = 1
                        for col in range(1, NUM_COLS):
                            if self.board.board[row][col] != 0 and self.board.board[row][col] == self.board.board[row][col-1]:
                                cell_val = self.board.board[row][col]
                                        count += 1
                                        if count >= 4:
                                            if cell_val == oppo:
                                                oppo_fours += 1
                                            else:
                                                my_fours += 1
                                                break
                                else:
                                    if count == 3:
                                        if cell_val == oppo:
                                            oppo_threes += 1
                                        else:
                                            my_threes += 1	
                                        elif count == 2:
                                            if cell_val == oppo:
                                                oppo_twos += 1
                                            else:
                                                my_twos += 1



                # Check vertical cells
                for col in range(NUM_COLS):
                    count = 1
                        for row in range(1, NUM_ROWS):
                            if self.board.board[row][col] != 0 and self.board.board[row][col] == self.board.board[row-1][col]:
                                cell_val = self.board.board[row][col]
                                        count += 1
                                        if count >= 4:
                                            if cell_val == oppo:
                                                oppo_fours += 1
                                            else:
                                                my_fours += 1
                                                break
                                else:
                                    if count == 3:
                                        if cell_val == oppo:
                                            oppo_threes += 1
                                        else:
                                            my_threes += 1	
                                        elif count == 2:
                                            if cell_val == oppo:
                                                oppo_twos += 1
                                            else:
                                                my_twos += 1


                # Check the lower diagonal from left edge to middle of board
                for i in range(3, NUM_COLS):
                    row = 1
                        col = i-1
                        count = 1
                        while row < NUM_ROWS and col > -1:
                            if self.board.board[row][col] != 0 and self.board.board[row][col] == self.board.board[row-1][col+1]:
                                cell_val = self.board.board[row][col]
                                        count += 1
                                        if count >= 4:
                                            if cell_val == oppo:
                                                oppo_fours += 1
                                            else:
                                                my_fours += 1
                                                break
                                else:
                                    if count == 3:
                                        if cell_val == oppo:
                                            oppo_threes += 1
                                        else:
                                            my_threes += 1	
                                        elif count == 2:
                                            if cell_val == oppo:
                                                oppo_twos += 1
                                            else:
                                                my_twos += 1

                                row += 1
                                col -= 1


                # Check the upper diagonal from left edge to middle of board
                for i in range(1, 4):
                    row = i+1
                        col = 4
                        count = 1
                        while row < NUM_ROWS and col > -1:
                            if self.board.board[row][col] != 0 and self.board.board[row][col] == self.board.board[row-1][col+1]:
                                cell_val = self.board.board[row][col]
                                        count += 1
                                        if count >= 4:
                                            if cell_val == oppo:
                                                oppo_fours += 1
                                            else:
                                                my_fours += 1
                                                break
                                else:
                                    if count == 3:
                                        if cell_val == oppo:
                                            oppo_threes += 1
                                        else:
                                            my_threes += 1	
                                        elif count == 2:
                                            if cell_val == oppo:
                                                oppo_twos += 1
                                            else:
                                                my_twos += 1

                                row += 1
                                col -= 1


                # Check the lower diagonal from right edge to middle of board
                for i in range(NUM_COLS-1, 2, -1):
                    row = 5
                        col = i-1
                        count = 1
                        while row > -1 and col > -1:
                            if self.board.board[row][col] != 0 and self.board.board[row][col] == self.board.board[row+1][col+1]:
                                cell_val = self.board.board[row][col]
                                        count += 1
                                        if count >= 4:
                                            if cell_val == oppo:
                                                oppo_fours += 1
                                            else:
                                                my_fours += 1
                                                break
                                else:
                                    if count == 3:
                                        if cell_val == oppo:
                                            oppo_threes += 1
                                        else:
                                            my_threes += 1	
                                        elif count == 2:
                                            if cell_val == oppo:
                                                oppo_twos += 1
                                            else:
                                                my_twos += 1

                                row -= 1
                                col -= 1

                # Check the upper diagonal from right edge to middle of board
                for i in range(NUM_ROWS-2, 2, -1):
                    row = i-1
                        col = 4
                        count = 1
                        while row > -1 and col > -1:
                            if self.board.board[row][col] != 0 and self.board.board[row][col] == self.board.board[row+1][col+1]:
                                cell_val = self.board.board[row][col]
                                        count += 1
                                        if count >= 4:
                                            if cell_val == oppo:
                                                oppo_fours += 1
                                            else:
                                                my_fours += 1
                                                break
                                else:
                                    if count == 3:
                                        if cell_val == oppo:
                                            oppo_threes += 1
                                        else:
                                            my_threes += 1	
                                        elif count == 2:
                                            if cell_val == oppo:
                                                oppo_twos += 1
                                            else:
                                                my_twos += 1

                                row -= 1
                                col -= 1

                return my_fours * 1000 + my_threes * 100 + my_twos - (oppo_fours * 1000 + oppo_threes * 100 + oppo_twos)
