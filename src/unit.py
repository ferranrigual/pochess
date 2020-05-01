from abc import ABC, abstractmethod

class Unit(ABC):
	
	def __init__(self, pos):
		super().__init__()
		self.char = "."
		self.pos = pos
	
	@abstractmethod
	def get_moves(self):
		pass
	
