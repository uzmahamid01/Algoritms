def mergeSort(arr):
    n = len(arr)
    if (n==1):
        return arr
    
    mid = n//2
    arr_left = arr[:mid]
    arr_right = arr[mid:]

    return merge(mergeSort(arr_left), mergeSort(arr_right))


def merge(arr_left, arr_right):
    i=0  # Index for left subarray
    j=0  # Index for right subarray
    sorted_arr = []  
    l = len(arr_left)
    r = len(arr_right)

    while (i < l and j<r):
        if  (arr_left[i] <= arr_right[j]):
            sorted_arr.append(arr_left[i])
            i = i + 1
        else:
            sorted_arr.append(arr_right[j])
            j = j + 1

    # If any element was left in left array then add it to the sorted array
    while (i < l):
        sorted_arr.append(arr_left[i])
        i = i+1

    # If any element was left in right array then add it to the sorted array
    while (j < r):
        sorted_arr.append(arr_right[j])
        j = j + 1
        
    return sorted_arr


print("Original Array : ", [38, 27, 43,  31, 56, 23, 49, 66, 78, 90])
print("\nSorted Array : ", mergeSort([38, 27, 43,  31, 56, 23, 49, 66, 78, 90]))
