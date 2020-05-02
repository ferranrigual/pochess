from board import board
from unit_warrior import Warrior
from unit_archer import Archer
from window import Window

import pygame

if __name__ == "__main__":

	pygame.init()

	#~ board = Board()
	#~ print(board)
	
	window = Window()
	window.init()

	pygame.event.set_blocked(pygame.MOUSEMOTION)

	archer = Archer((0, 3))
	board.add_unit(archer)
	archer = Archer((0, 4))
	board.add_unit(archer)
	warrior = Warrior((1, 3))
	board.add_unit(warrior)
	warrior = Warrior((1, 4))
	board.add_unit(warrior)

	archer = Archer((7, 3))
	board.add_unit(archer)
	archer = Archer((7, 4))
	board.add_unit(archer)
	warrior = Warrior((6, 3))
	board.add_unit(warrior)
	warrior = Warrior((6, 4))
	board.add_unit(warrior)

	fps = 20
	run = True
	while run:
		pygame.time.delay(int(1000/fps)) # ms

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			else:
				window.handle_event(event)

		window.display()

	pygame.quit()


