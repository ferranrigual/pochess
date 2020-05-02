from unit import Unit

class Warrior(Unit):
	
	def __init__(self, pos):
		super().__init__(pos)
		self.char = "W"
		self.max_hp = 2
		self.hp = self.max_hp

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
		attacks.append((-1, -1))
		attacks.append((-1, 0))
		attacks.append((-1, +1))
		attacks.append((0, -1))
		attacks.append((0, +1))
		attacks.append((+1, -1))
		attacks.append((+1, 0))
		attacks.append((+1, +1))
		return attacks
