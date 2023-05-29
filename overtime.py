hours = input('Enter hours worked:\n')
rate = input('Enter rate of pay:\n')
try:
    if float(hours) > 40 :
        grossPay = 40*float(rate)+((float(hours)-40)*(float(rate)*1.5))
    else :
        grossPay = float(hours)*float(rate)
    print('Gross pay amount:',grossPay)
except:
    print('Please run the program again and limit your input to numerical values.')
