import random 
class Pokemon():
	def __init__ (self, pokemon_type, name, cp, hp):
		self.pokemon_type = pokemon_type
		self.name = name
		self.cp = cp
		self.hp = hp
	def get_status (self):
		return self.name + str(self.cp) + str(self.hp)
	def new_name (self, new_name):
		self.name = new_name
	def increase_cp (self, amount):
		self.cp += amount 
	def decrease_cp (self, amount):
		self.cp -= amount
	def is_attacked (self, damage):
		self.hp -= damage
	def attack(self, another, attack_strength):
		success=random.rand_int(0,3)
		if success == 1:
			if cp <20:
				attack_strength = attack_strength*1
			elif cp <= 40 and cp >= 20:
				attack_strength = attack_strength*2
			elif cp <=60 and cp >= 40:
				attack_strength = attack_strength*3
			elif cp <=80 and cp >= 60:
				attack_strength = attack_strength*4
			elif cp <=100 and cp >= 80: 
				attack_strength = attack_strength*5	
			another.is_attacked(attack_strength)

			print("You won the battle!")	
			self.get_status()
			print(self.get_status())
		else:
			print("You lost the battle loser. HAHAHAHA")
			self.decrease_cp()
class eevee(Pokemon):
	