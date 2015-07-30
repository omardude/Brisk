import Brisk.Brisk;

class GamePlayer:
	def __init__(self):
		self.brisk = Brisk();
		self.map = Map(brisk)
		self.me = Player_Status(brisk, self.map, true)
		
		# self.enemy_player_state = Player_State()

	def start(self):
		brisk = Brisk();
		while True():
			player_state = brisk.get_player_status()
			if player_state['current_turn']:
				self.take_turn(player_stateus)

	def update_information(self, player_state_response):
		self.me.update(player_state_response)
		# self.enemy_player_state.update(asdf)update

	def place_armies(self):
		num_reserves = self.me.num_reserves
		self.brisk.place_armies(self.me.territories[0].id, num_reserves)

	def launch_attack(self):
		for territory in me.territories:
			if territory.adjacent_territories.length > 1:
				adjacent_territory = territory.adjacent_territories[0]
				self.brisk.attack(territory.id, adjacent_territory.territory, min(3, territory.num_armies))
				break

	def take_turn(self):
		self.update_information()
		# get first territory that is available
		self.place_armies()

		self.launch_attack()

		self.brisk.end_turn()


class Map:
	def __init__(self, brisk):
		self.brisk = brisk
		self.update()

	def update(self, params = None):
		if not params:
			params = self.brisk.get_map_image()
		self.territories = params['terirtories']
		self.version = params['version']
		self.continents = params['continents']
		self.serivce = params['service']


class Player_Status:

	def __init__(self, brisk, map, is_me):
		self.brisk = brisk
		self.map = map
		# if is_me:
		self.update()
		# else:
		# 	self.update(self.brisk.get_enemy_player_state())

	def update(self, params=None):
		if not params:
			params = self.brisk.get_player_status()
		self.version = params['version']
		self.service = params['service']
		self.game = params['game']
		self.player = params['player']
		self.current_turn = params['current_turn']
		self.eliminated = params['eliminated']
		self.winner = params['winner']
		self.num_armies = params['num_armies']
		self.num_reserves = params['num_reserves']
		self.territories = []
		for territory in params['territories']:
			self.territories.append( Territory(territory['territory'], territory['num_armies']), self )

class Territory:
	def __init__(self, params, player_state):
		self.id = params['territory']
		self.num_armies = params['num_armies']
		self.owner = player_state
		self.brisk = self.owner.brisk
		self.map = self.owner.map
		self.adjacent_territories = self.map[self.territory_identifier]