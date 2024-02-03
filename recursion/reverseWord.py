def reverseWord(str):
    words = list(str)
    reverseWord = []

    def addToArray(array):
        if(len(array)>0):
            reverseWord.append(array.pop())
            addToArray(array)

    addToArray(words)
    result = ''.join(reverseWord)
    return result


print(reverseWord("yoyo master"))
