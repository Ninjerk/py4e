str = 'X-DSPAM-Confidence: 0.8475 '

startIndex = str.find(' ')
#print(startIndex)
lastIndex = str.find(' ',startIndex+1)
#print(lastIndex)

confidence = str[startIndex+1:lastIndex]
#print(confidence)
print(float(confidence))
