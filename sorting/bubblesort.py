def bubbleSort(array):
    n = len(array)
    #iterates through each element of an array 
    for  i in range(n):
        #compares adjacent array and swaps based on conditions
        for j in range(n-i-1):
            if(array[j]>array[j+1]):
                #swap
                array[j],array[j+1]=array[j+1],array[j]
    return  array            


arr = [64, 34, 25, 12,  22, 11, 90]
print("Original array is:", arr)
sorted_arr = bubbleSort(arr)
print("Sorted array is:", sorted_arr)

