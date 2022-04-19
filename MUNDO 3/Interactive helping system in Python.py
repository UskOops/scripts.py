from time import sleep as sl
def PyHELP():
	while True:
		print('~' * 25,   'HELP SYSTEM PyHELP' , '~' * 25)
		function = str(input('\nFunction or library: '))
		if(function == 'end'):
			print('Thanks for using our program!!')
			break
		else:
			print('Loading...')
			sl(0.5)
			print(help(function))

PyHELP()