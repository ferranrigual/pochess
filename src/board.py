from unit import Unit

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
			print("WARN", r, c)
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

	def add_unit(self, unit):
		pos = unit.pos
		r, c = pos
		if self.cells[r][c] != None:
			raise "Can not add unit. Cell is not empty"
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
	
	def __str__(self):
		for r in range(self.size):
			for c in range(self.size):
				if self.cells[r][c] == None:
					print(".", end="")
				else:
					print("U", end="")
			print()
		
board = Board()
