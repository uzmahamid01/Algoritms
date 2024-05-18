#return the first non repeating letter in a string
def  find_non_repeat(string):
    hashmap = {}
    
    #input = "abcade"  -- output of this  function should be 'b' because it is the first character that appears once.
    for char in string:
        if char in  hashmap:
            hashmap[char] +=1
        else:
            hashmap[char] = 1

    for k in  hashmap.keys():
        if hashmap[k]==1 : 
            return k
    return None

# Testing the function
print(find_non_repeat("loveleetcode"))  
print(find_non_repeat("abcade"))

