import board
import random


def perft(board, depth):
	# Node at depth d
	if depth == 0:
		return 1

	# Terminal node
	if board.last_move_won():
		return 1
	
	# Non-terminal node and depth < d
	available_moves = board.generate_moves()
	sum = 0
	for move in available_moves:
		board.make_move(move)
		sum += perft(board, depth-1)
		board.unmake_last_move()

	return sum


def find_win(board, depth):
	value, next_move = alpha_beta_negamax_root(board, depth, float('-inf'), float('inf'))
	if value == 1:
		return "WIN BY PLAYING %r" % next_move
	elif value == -1:
		return "ALL MOVES LOSE"
	else:
		return "NO FORCED WIN IN %r MOVES" % depth


def alpha_beta_negamax_root(board, depth, alpha, beta):
	if board.last_move_won():
		return board.turn * 1, None
	if depth == 0:
		return 0, None
	next_move = None
	available_moves = board.generate_moves()
	for move in available_moves:
		board.make_move(move)
		v, nm = alpha_beta_negamax_root(board, depth-1, -beta, -alpha)
		v *= -1
		board.unmake_last_move()
		if v >= beta:
			return beta, move
		elif v > alpha:
			alpha = v
			next_move = move
	return alpha, next_move
