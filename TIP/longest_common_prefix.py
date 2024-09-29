def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    one = strs[0]
    two = strs[1]
    three = strs[2]

    s = ""

    for i in range(len(one)):
        for j in range(len(two)):
            for k in range(len(three)):
                if one[i] == two[j] == three[k]:
                    s += one[i]
    return s

def main():
    strs = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    print(longestCommonPrefix(strs))
    print(longestCommonPrefix(strs2))
    return 0
main()

