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

'''If the input string is not empty, the function recursively calls itself with the substring starting from the second 
character (str.substr(1)), and then concatenates the first character (str.charAt(0)) at the end. '''

def reverse(str):
    if str == "":
        return ""
    return reverse(str[1:]) + str[0]

print(reverse("yoyo master"))