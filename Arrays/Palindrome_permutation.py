#Time Complexity = O(n)

def palindrome_perm(string):
    # string = list(str)
    # print(string)
    # for i in range(len(string)):
    #     if string[i] in string[i+1:]:
    #         string.remove(string[i])
            
    #     else:
    #         return False
    #     return True
    str = string.replace(" ", "").lower()
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    odd_count = 0
    for char in char_count:
        if char_count[char] % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
            return True

    

def main():
    print(palindrome_perm("tact coa"))

main()
    
    