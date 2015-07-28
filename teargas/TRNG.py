
'''
List of functions:
	
	1. trng()             -              A true random number generator utilising data corruption. Data corruption occurs
	                                           in number.num file (specified in variable num_gen).


                       ---If you want to compile this script,                       
                       		***This file MUST be compiled in speical way to ensure right behaviour!!!***
                        	***That special way is providing an environment guaranteeing thread racing***

'''

from threading import Thread


def generate():
	num_gen = 'tear_gas/number.num'

	def zero():
		with open (num_gen, 'a') as opener:
			opener.write('0')

	def one():
		with open (num_gen, 'a') as opener:
			opener.write('1')

	def two():
		with open (num_gen, 'a') as opener:
			opener.write('2')

	def three():
		with open (num_gen, 'a') as opener:
			opener.write('3')

	def four():
		with open (num_gen, 'a') as opener:
			opener.write('4')

	def five():
		with open (num_gen, 'a') as opener:
			opener.write('5')

	def six():
		with open (num_gen, 'a') as opener:
			opener.write('6')

	def seven():
		with open (num_gen, 'a') as opener:
			opener.write('7')

	def eight():
		with open (num_gen, 'a') as opener:
			opener.write('8')

	def nine():
		with open (num_gen, 'a') as opener:
			opener.write('9')

	def first():
		thread_1=Thread(target=one)
		thread_2=Thread(target=two)
		thread_3=Thread(target=three)
		thread_4=Thread(target=four)
		thread_5=Thread(target=five)
		thread_6=Thread(target=six)
		thread_7=Thread(target=seven)
		thread_8=Thread(target=eight)
		thread_1.start()
		thread_2.start()
		thread_3.start()
		thread_4.start()
		thread_5.start()
		thread_6.start()
		thread_7.start()
		thread_8.start()

	def second():
		thread_1=Thread(target=nine)
		thread_2=Thread(target=seven)
		thread_3=Thread(target=six)
		thread_4=Thread(target=five)
		thread_5=Thread(target=four)
		thread_6=Thread(target=three)
		thread_7=Thread(target=two)
		thread_8=Thread(target=zero)
		thread_1.start()
		thread_2.start()
		thread_3.start()
		thread_4.start()
		thread_5.start()
		thread_6.start()
		thread_7.start()
		thread_8.start()

	def third():
		thread_1=Thread(target=zero)
		thread_2=Thread(target=one)
		thread_3=Thread(target=three)
		thread_4=Thread(target=four)
		thread_5=Thread(target=five)
		thread_6=Thread(target=six)
		thread_7=Thread(target=eight)
		thread_8=Thread(target=nine)
		thread_1.start()
		thread_2.start()
		thread_3.start()
		thread_4.start()
		thread_5.start()
		thread_6.start()
		thread_7.start()
		thread_8.start()

	def fourth():
		thread_1=Thread(target=nine)
		thread_2=Thread(target=eight)
		thread_3=Thread(target=seven)
		thread_4=Thread(target=five)
		thread_5=Thread(target=four)
		thread_6=Thread(target=two)
		thread_7=Thread(target=one)
		thread_8=Thread(target=zero)
		thread_1.start()
		thread_2.start()
		thread_3.start()
		thread_4.start()
		thread_5.start()
		thread_6.start()
		thread_7.start()
		thread_8.start()

	def fifth():
		thread_1=Thread(target=zero)
		thread_2=Thread(target=one)
		thread_3=Thread(target=two)
		thread_4=Thread(target=three)
		thread_5=Thread(target=six)
		thread_6=Thread(target=seven)
		thread_7=Thread(target=eight)
		thread_8=Thread(target=nine)
		thread_1.start()
		thread_2.start()
		thread_3.start()
		thread_4.start()
		thread_5.start()
		thread_6.start()
		thread_7.start()
		thread_8.start()

	def thread_set():
		thread_1=Thread(target=first)
		thread_2=Thread(target=second)
		thread_3=Thread(target=third)
		thread_4=Thread(target=fourth)
		thread_5=Thread(target=fifth)
		thread_1.start()
		thread_2.start()
		thread_3.start()
		thread_4.start()
		thread_5.start()

	ithread_1=Thread(target=thread_set)
	ithread_2=Thread(target=thread_set)
	ithread_1.start()
	ithread_2.start()

	reader=open(num_gen, 'r').read()

	with open(num_gen, 'w') as opener:
		opener.write('')

	return int(reader)

#---------------------------------------------------------------

def trng():
	while  True:
		try:
			return generate()
		except:
			pass