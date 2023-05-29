def computepay(hours, rate):
	if float(hours) > 40 :
		gross = (40 * float(rate)) + ((float(hours) - 40)*(float(rate)*1.5))
		return gross
	else :
		gross = float(hours)*float(rate)
		return gross
		
hours = input('Please enter hours worked\n')
rate = input('Please enter payrate\n')
print('Gross pay:',computepay(hours, rate))