from unit import Unit

class Archer(Unit):
	
	def __init__(self, pos):
		super().__init__(pos)
		self.char = "A"

	def get_moves(self):
		moves = []
		moves.append((-1, -1))
		moves.append((-1, 0))
		moves.append((-1, +1))
		moves.append((0, -1))
		moves.append((0, +1))
		moves.append((+1, -1))
		moves.append((+1, 0))
		moves.append((+1, +1))
		return moves

	def get_attacks(self):
		attacks = []
		for r in [-2, 2]:
			for c in range(-2, 3):
				attacks.append((r,c))
		for c in [-2, 2]:
			for r in range(-1, 2):
				attacks.append((r,c))
		return attacks
