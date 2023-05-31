total = 0
count = 0
while True:
    try :
        running = input('Enter a number:')
        if running == 'done' :
            break
        total = total + float(running)
        count = count + 1
    except :
        print('Please enter a number\n')

print(total, count, (total/count))