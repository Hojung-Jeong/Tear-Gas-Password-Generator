import random

from tear_gas.TRNG import trng


def tgpg(password_length=20):
	holder=[]

	while True:
		raw=trng()%127

		if raw>=33 and raw<127:
			holder.append(chr(raw))
		
		if len(holder)==password_length:
			joined=''.join(holder)
			return joined