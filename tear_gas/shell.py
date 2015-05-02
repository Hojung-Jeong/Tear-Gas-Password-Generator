import random

from tear_gas.propellant import propellant


def throw_it(password_length=20):
	ascii_buffer=33

	base=[propellant()%93 for num in range(password_length)]
	holder=[]

	for element in base:
		decider=(propellant()*propellant())%2

		if decider is 0:
			holder.append(chr(element+33))
		else:
			holder.append(element%10)

	joined=''.join(map(str, holder))
	return joined