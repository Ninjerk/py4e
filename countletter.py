def count(word, letter) :
    #word = 'banana'
    count = 0
    for characters in word:
        if characters == letter:
            count = count + 1
    print(count)

count(input('Enter a word:'), input('Select a letter to count:'))
