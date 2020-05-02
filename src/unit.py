from abc import ABC, abstractmethod

class Unit(ABC):
	
	def __init__(self, pos, team):
		super().__init__()
		self.char = "."
		self.pos = pos
		self.hp = 0
		self.max_hp = 0
		self.team = team
	
	@abstractmethod
	def get_moves(self):
		pass
	
	@abstractmethod
	def get_attacks(self):
		pass
	
	def attack(self, target):
		target.hp -= 1
	
	def is_damaged(self):
		return self.hp < self.max_hp
