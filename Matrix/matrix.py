#Declaration of the matrix:
numRows = 3
numCols = 3

arr = [[4] * numCols]*numRows
print(arr)

#initializing the matrix:
arr1 = [[1,2,3], [4, 5, 6], [7, 8, 9]]
print(arr1)

# Access elements of Matrix: using the indices 
print(arr1[0][2])

# Traversal of a Matrix: using two for loops
for i in range(len(arr1)):
    for j in range(len(arr1)):
        print(arr1[i][j], end=" ")
    print("")


# Searching in a Matrix: by traversing through all the elements 
def searchMatrix(arr1, x):
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if arr1[i][j] == x:
                return print("found " , arr1[i][j], end=" ")
            return print(x, " not found")
searchMatrix(arr1, 10)

# Sorting a Matrix: using two ways either row-wise or column wise
#Row-wise:
#Method 1: use Bubble sort: iterating through each row and sort elements using sorting algorithm
#Time: O(r*c*max(r,c))
#Auxiliary Space: O(1), since no extra space has been taken.
#lets go stepwise
#loop through rows 
    #loop through cols
        #loop for comparison and swap
            #swap
arr2 = [[9, 8, 7, 1 ],[7, 3, 0, 2],[9, 5, 3, 2],[ 6, 3, 1, 2 ]]
def RowSort(arr2):
    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            for k in range(len(arr2[i])-j-1):
                if (arr2[i][k] > arr2[i][k+1]):
                    t = arr2[i][k]
                    arr2[i][k] = arr2[i][k+1]
                    arr2[i][k+1] = t


    for i in range(len(arr2)):
        for j in range(len(arr2)):
            print(arr2[i][j], end=" ")
        print("")

RowSort(arr2)
print("----------------------------------------------------------")

#Method2: Using the library function .sort() for every row of the matrix:
#Time Complexity: O(r*c*log(c))
#Auxiliary Space: O(1)
def sortRow(arr2):
    for i in range(len(arr2)):
        arr2[i].sort()

for i in range(len(arr2)):
        for j in range(len(arr2)):
            print(arr2[i][j], end=" ")
        print("")

sortRow(arr2)



