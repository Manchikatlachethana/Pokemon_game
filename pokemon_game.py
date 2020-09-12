from random import randint

# create a list of play options
pokemons=['squirtle','charmander','bulbasaur']
print("Welcome to lockdown battle league!!!")
while True:
	c_index=randint(0,2)
	c_choice=pokemons[c_index]
	user_choice=input("Choose your Pokemon for battle: squirtle, charmander, bulbasaur:\n")
	print("Team Rocket pokemon:", c_choice)
	print("Ash's pokemon:", user_choice)
	if user_choice==c_choice:
		print("Ash and Team Rocket tie")
	elif user_choice=='squirtle' and c_choice=='charmander':
		print('Ash won!\nsquirtles hydro pump attacked charmander')
	elif user_choice=='charmander' and c_choice=='bulbasaur':
		print("Ash won!\n charmander's flame throws bulbasaur down..." )
	elif user_choice=='bulbasaur' and c_choice=='squirtle':
		print("Ash won!\nsquirtle cannot come out of bulbasaurs vine whip")
	else:
		print('Team Rocket won!!!')
	user_continue=input('Ash! do you wanna have another Round ?:(y/n)')
	if user_continue=='n':
		break