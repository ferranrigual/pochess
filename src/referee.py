
class Referee():
	def __init__(self):
		self.actions_per_turn = 3
		self.number_of_teams = 2
		self.current_turn = 0
		self.current_action = 0
		pass
	
	def get_current_team(self):
		return self.current_turn % self.number_of_teams
	
	def spent_action(self):
		self.current_action += 1
		if self.current_action == self.actions_per_turn:
			self.current_action = 0
			self.current_turn += 1
	
	def get_pending_actions(self):
		return self.actions_per_turn - self.current_action
		
referee = Referee()

