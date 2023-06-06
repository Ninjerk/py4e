fhand = open('mbox-short.txt')
#print(type(fhand))

for line in fhand :
    print(line.upper().strip('\n')) #.strip('\n') added as print() adds an additional newline character