def get_placa():
	import random
	# RETORNA 1 LETRA DO ALFABETO EM UPPERCASE
	def letter_gen():
		import string
		letter = random.choice(string.ascii_uppercase)
		return str(letter)
		
	# RETORNA 1 NUMERO DE 0 A 9
	def number_gen():
		number = random.choice("0123456789")
		return str(number)
		
	# GERADOR PLACA MERCOSUL
	def placa_gen_merc():
		pl = []
		for x in range(7):
			if len(pl) <= 1 or len(pl) == 2:
				pl.append(letter_gen())
			elif len(pl) == 3:
				pl.append(number_gen())
			elif len(pl) == 4:
				pl.append(letter_gen())
			elif len(pl) > 4:
				pl.append(number_gen())
		return ''.join(pl)
		
	# GERADOR PLACA ANTIGA
	def placa_gen_ant():
		pl = []
		for x in range(7):
			if len(pl) <= 1 or len(pl) == 2:
				pl.append(letter_gen())
			elif len(pl) > 2:
				pl.append(number_gen())
		return ''.join(pl)
		
	# ESCOLHE PLACA ANTIGA OU MERCOSUL
	gerpl = (placa_gen_merc(), placa_gen_ant())
	return random.choice(gerpl)
	
print(get_placa())