total = 0
count = 0
lowest = None
highest = None
while True:
    try :
        running = input('Enter a number:')
        if running == 'done' :
            break
        total = total + float(running)
        count = count + 1
    except :
        print('Please enter a number\n')
        
    #**In the following comparions, arguments(?) were being evaluated as STRINGS, and so highest was not being set after '9'**
    if lowest is None or float(running) < float(lowest) :
        print(lowest,' before setting new low')
        lowest = running
        print(lowest,' after setting new low')
    if highest is None or float(running) > float(highest) :
        print(highest,' before setting new high')
        highest = running
        print(highest,' after setting new high')

print(total, count, lowest, highest)