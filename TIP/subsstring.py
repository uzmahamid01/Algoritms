
def subString(arr):
    s1 = sorted(arr[0])
    s2 = sorted(arr[1])

    if len(s2) > len(s1):
        return False 
    
    # for i in range(len(s1)):
    #     if s2[i] in s1:
    #         return True

    l1 = 0
    l2 = 0

    while l1 < len(s1) and l2 < len(s2):
        if s1[l1] == s2[l2]:
            l2 += 1
        l1 += 1
        
    return l2 == len(s2)

            

def main():
    arr1 = ['laboratory', 'rat']
    arr2 = ['cat', 'meow']
    arr3 = ['catdog', ""]
    print(subString(arr1))
    print(subString(arr2))
    print(subString(arr3))

main()


