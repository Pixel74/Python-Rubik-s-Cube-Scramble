def scramble_generator(nmoves=12):
	import random
	moves = ('U', "U'", 'U2', 'D', "D'", 'D2', 'L', "L'", 'L2', 'R', "R'", 'R2', 'F', "F'", 'F2', 'B', "B'", 'B2')
	output = []
	for n in range(0, nmoves):
		output.append(moves[random.randint(0, len(moves)-1)])
	return output

#print(scramble_generator())