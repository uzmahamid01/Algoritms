def selectionSort(arr):
    n = len(arr)
    i = 0
    while i < n:
        min = arr[i]
        index = i
        for j in range(i+1, n):
            if arr[j]<min:
                index = j
                min = arr[j]
        arr[i], arr[index] = arr[index], arr[i]

        i+=1
    return arr


print("Original array:", [45, 23, 16,  78, 90])
sorted_array = selectionSort([45, 23, 16, 78, 90])
print("\n\nSorted array: ", sorted_array)