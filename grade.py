try:
	grade = input('Enter score:\n')
	if float(grade) < 0.6:
		print('F')
	elif float(grade) >= 0.6 and float(grade) < 0.7:
		print ('D')
	elif float(grade) >= 0.7 and float(grade) < 0.8:
		print ('C')
	elif float(grade) >= 0.8 and float(grade) < 0.9:
		print ('B')
	elif float(grade) >= 0.9 and float(grade) < 1.0:
		print ('A')
	elif float(grade) < 0.0:
		print ('Score must be greater than zero.')
	elif float(grade) >= 1.0:
		print ('Score must be between 0.0 and 1.0')
except:
	print('Please limit input to numerical values')