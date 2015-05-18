import random

from tear_gas.propellant import propellant


def throw_it(password_length=20):
	holder=[]

	while True:
		raw=propellant()%123

		if raw>47 and raw<58:
			holder.append(chr(raw))
		elif raw>64 and raw<91:
			holder.append(chr(raw))
		elif raw>96 and raw<123:
			holder.append(chr(raw))
		
		if len(holder)==password_length:
			joined=''.join(holder)
			return joined