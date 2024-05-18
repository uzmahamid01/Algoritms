#overall complexity = O(n)
#compression space compl. = O(k)
#compression2 space compl. = O(1)

#input = aabcccccaaa = a5b1c5
def compression(string):
    hashtable = {}
    for char in string:
        if char in hashtable:
            hashtable[char] += 1
        else:
            hashtable[char] = 1

    compressed_str = ""
    for key, val in hashtable.items():
        compressed_str += str(key) + str(val)
        #print(key, val)
    return compressed_str


#input = aabcccccaaa = a2b1c5a3
def compression2(string):
    compressed_str = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed_str += string[i-1] + str(count)
            count = 1
        
    compressed_str += string[-1] + str(count)
    return compressed_str

def main():
    user_input = input("Enter a string: ")
    compressed_string = compression(user_input)
    print("The compressed string is:", compressed_string)
    compressed_string2 = compression2(user_input)
    print("The compressed string is:", compressed_string2)

main()
