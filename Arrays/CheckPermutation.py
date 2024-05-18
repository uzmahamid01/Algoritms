

# Metho1:  sort and compare
# def checkperm(str1, str2):
#     if len(str1) != len(str2):
#         return False
    
#     str1 = sorted(str1)
#     str2 = sorted(str2)
    
#     for i in range(len(str1)):
#         if str1[i] != str2[i]:
#             return False
#     return True
    

# Method2: count and compare
total_chars = 256
def checkperm(str1, str2):

    count1 = [0] * total_chars
    count2 = [0] * total_chars

    for i in range(len(str1)):
        count1[ord(str1[i])] += 1


    for i in range(len(str2)):
        count2[ord(str2[i])] += 1
    
    if len(str1) != len(str2):
        return False
    
    for i in range(total_chars):
        if count1[i] != count2[i]:
            return False
    return True
 

def main():
    str1 = "1"
    str2 = "84"
    str3 = "122"
    str4 = "221"
    print(checkperm(str1, str2))   
    print(checkperm(str2, str3))
    print(checkperm(str1, str3))
    print(checkperm(str1, str4))
    print(checkperm(str3, str4))
    print(checkperm(str2, str4))

main()