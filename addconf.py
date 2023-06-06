fname = input('Enter file name:')
fhand = open(fname)
total = 0

def numSlice(slicee):
    startIndex = slicee.find(' ')
    lastIndex = slicee.find(' ',startIndex+1)
    addend = slicee[startIndex+1:lastIndex]
    print(addend)
    return addend
	
for line in fhand:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
            numSlice(line)
            print(line)
    #print(line)