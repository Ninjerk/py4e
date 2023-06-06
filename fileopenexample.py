#This is an example pulled from the discussion section in order to compare results.
fname = input('Enter the file name: ')
try :
    fhand = open(fname)
except:
    print('File connot be opened:',fname)
    exit()

inp = fhand.read()
print(inp.upper())