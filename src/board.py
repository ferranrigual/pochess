from unit import Unit
from referee import referee

class Board():
	
	def __init__(self):
		super().__init__()
		self.size = 8
		self.cells = [[None]*8 for _ in range(8)]
	
	def get_unit(self, cell):
		r, c = cell
		return self.cells[r][c]
	
	def is_empty(self, cell):
		r, c = cell
		return self.cells[r][c] == None
		
	def get_moves(self, cell):
		r, c = cell
		unit = self.cells[r][c]
		if unit == None:
			raise Exception("Can not get moves. Cell is empty")
		
		# check if it's this unit's turn
		if unit.team != referee.get_current_team():
			return []

		moves = unit.get_moves()
		
		dests = []
		for move in moves:
			dr = r + move[0]
			dc = c + move[1]
			
			# check bounds
			if dr < 0 or dc < 0 or dr >= self.size or dc >= self.size:
				continue
			
			# check empty
			if self.cells[dr][dc] != None:
				continue
			
			dests.append((dr, dc))
		
		return dests

	def get_attacks(self, cell):
		r, c = cell
		unit = self.cells[r][c]
		if unit == None:
			raise Exception("Can not get attacks. Cell is empty")
		
		# check if it's this unit's turn
		if unit.team != referee.get_current_team():
			return []
		
		targets = []
		for attack in unit.get_attacks():
			dr = r + attack[0]
			dc = c + attack[1]
			
			# check bounds
			if dr < 0 or dc < 0 or dr >= self.size or dc >= self.size:
				continue
			
			# check empty
			if self.cells[dr][dc] == None:
				continue
			
			# check not same team
			if unit.team == self.cells[dr][dc].team:
				continue
			
			targets.append((dr, dc))
		
		return targets

	def add_unit(self, unit):
		pos = unit.pos
		r, c = pos
		if self.cells[r][c] != None:
			raise Exception("Can not add unit. Cell is not empty")
		self.cells[r][c] = unit
	
	def move_unit(self, orig, dest):
		unit = self.get_unit(orig)
		
		if unit == None:
			raise Exception("Can not move unit. Orig is empty")
		if self.get_unit(dest) != None:
			raise Exception("Can not move unit. Dest is not empty")

		unit.pos = dest
		r, c = orig
		self.cells[r][c] = None
		r, c = dest
		self.cells[r][c] = unit
		
		referee.spent_action()
	
	def attack_unit(self, orig, dest):
		unit = self.get_unit(orig)
		
		if unit == None:
			raise Exception("Can not attack unit. Orig is empty")
		if self.get_unit(dest) == None:
			raise Exception("Can not attack unit. Dest is empty")
		
		r, c = dest
		dest_unit = self.cells[r][c]
		unit.attack(dest_unit)
		if dest_unit.hp <= 0:
			self.cells[r][c] = None
		
		referee.spent_action()

	def is_game_ended(self):
		surviving_teams = set()
		for r in range(self.size):
			for c in range(self.size):
				unit = self.cells[r][c]
				if unit == None:
					continue
				surviving_teams.add(unit.team)
		return len(surviving_teams) == 1
		
	def __str__(self):
		for r in range(self.size):
			for c in range(self.size):
				if self.cells[r][c] == None:
					print(".", end="")
				else:
					print("U", end="")
			print()
		
board = Board()
