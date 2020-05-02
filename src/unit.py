from abc import ABC, abstractmethod

class Unit(ABC):
	
	def __init__(self, pos):
		super().__init__()
		self.char = "."
		self.pos = pos
		self.hp = 0
		self.max_hp = 0
	
	@abstractmethod
	def get_moves(self):
		pass
	
	@abstractmethod
	def get_attacks(self):
		pass
	
	def receive_attack(self, damage):
		self.hp -= damage
	
	def is_damaged(self):
		return self.hp < self.max_hp
