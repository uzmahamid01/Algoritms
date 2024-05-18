def diffSet(l1, l2):
    hashmap2 = {}
    for num in l1:
        if num in l2:
            continue
        else:
            hashmap2[num] = num

    for num in l2:
        if num in l1:
            continue
        else:
            hashmap2[num] = num
    
    return list(hashmap2)

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    
    result = diffSet(list1, list2)
    print("Difference set:", result)

if __name__ == "__main__":
    main()

            