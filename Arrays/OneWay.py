def oneAway(str1, str2):
    if len(str1) == len(str2):
        return replaceOne(str1, str2)
    elif len(str1)+1 == len(str2) :
        return insertOne(str1, str2)
    elif len(str1)-1 == len(str2) :
        return insertOne(str2, str1)
    else:
        return False


    
def replaceOne(str1, str2):
    diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if diff:
                return False
            diff = True
    return True



def insertOne(str1, str2):
    index1 = 0
    index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def main():
    print(oneAway("pale", "ple"))

main()