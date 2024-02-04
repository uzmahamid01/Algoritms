def insertionSort(arr):
    n = len(arr)
    for  i in range(n):
        if arr[i] < arr[0]:
            arr.insert(0, arr.pop(i))
        else:
            for j in range(1,i):
                if  arr[j] > arr[j-1] and arr[i] < arr[j]:
                    arr.insert(j, arr.pop(i))
                
    return arr

print("Insertion Sort")
randomList = [45,23,98,17,65,21,74,36,83]
print("Original List : ", randomList)
sortedList = insertionSort(randomList)
print("Sorted List   : ", sortedList)

