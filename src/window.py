from board import board
from unit import Unit
from referee import referee

import pygame

def init_image_dict():
	d = {}
	d["W0"] = pygame.image.load("res/units/warrior_0.png")
	d["A0"] = pygame.image.load("res/units/archer_0.png")
	d["W1"] = pygame.image.load("res/units/warrior_1.png")
	d["A1"] = pygame.image.load("res/units/archer_1.png")
	return d

class Window():
	
	def __init__(self):
		super().__init__()
		self.win = None

		self.w = 640
		self.h = 480
		self.margin = 2

		self.cell_size = None
		
		self.selected_cell = None
		self.moving_cells = []
		self.attacking_cells = []
		
	def init(self):
		self.cell_size = int((min(self.w, self.h) - self.margin) / board.size - self.margin)
		pygame.display.set_caption("PoChess game")
		self.win = pygame.display.set_mode((self.w, self.h))
		
		self.img_dict = init_image_dict()
		
		self.board_right_end = board.size*(self.margin+self.cell_size) + self.margin
	
	def get_cell_from_pos(self, pos):
		x, y = pos
		c = int(x/(self.cell_size+self.margin))
		r = int(y/(self.cell_size+self.margin))
		return (r, c)
	
	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			cell = self.get_cell_from_pos(pos)

			if self.selected_cell == None:
				if board.is_empty(cell):
					return
				self.selected_cell = cell
				self.moving_cells = board.get_moves(cell)
				self.attacking_cells = board.get_attacks(cell)
				return
		
			if cell in self.moving_cells:
				board.move_unit(self.selected_cell, cell)
				self.selected_cell = None
				self.moving_cells = []
				self.attacking_cells = []
				return
			
			if cell in self.attacking_cells:
				board.attack_unit(self.selected_cell, cell)
				self.selected_cell = None
				self.moving_cells = []
				self.attacking_cells = []
				return
			
			self.selected_cell = None
			self.moving_cells = []
			self.attacking_cells = []
			
	
	def display(self):
		self.win.fill((0,0,0))
		
		self.display_board()
		self.display_game_info()
		
		pygame.display.update()

	def display_board(self):
		s = board.size
		m = self.margin
		cs = self.cell_size
		for r in range(s):
			for c in range(s):
				if (r,c) in self.moving_cells:
					color = (150,255,150)
				elif self.selected_cell == (r,c):
					color = (150,150,255)
				elif (r,c) in self.attacking_cells:
					color = (255,150,150)
				else:
					color = (255,255,255)
				pygame.draw.rect(self.win, color, (m+(m+cs)*c, m+(m+cs)*r, cs, cs))
				
				unit = board.cells[r][c]
				if unit != None:
					self.display_unit(unit)

	def display_unit(self, unit):
		s = board.size
		m = self.margin
		cs = self.cell_size

		r, c = unit.pos
		image = self.img_dict[unit.char + str(unit.team)]
		image = pygame.transform.scale(image, (cs, cs))
		
		px = int(m+(m+cs)*c)
		py = int(m+(m+cs)*r)
		self.win.blit(image, (px,py))
		
		# show HP
		color = (0,255,0)
		if unit.is_damaged():
			color = (255,0,0)
		font = pygame.font.SysFont(None, 32)
		text = font.render(str(unit.hp), True, color)
		text_pos = px, py
		self.win.blit(text, text_pos)

	def display_game_info(self):
		color = (255,255,255)
		font = pygame.font.SysFont(None, 20)

		text = font.render("Current turn: {}".format(referee.current_turn), True, color)
		text_pos = self.board_right_end, self.margin
		self.win.blit(text, text_pos)

		text = font.render("Pending actions: {}".format(referee.get_pending_actions()), True, color)
		text_pos = self.board_right_end, 2*self.margin + text.get_height()
		self.win.blit(text, text_pos)

