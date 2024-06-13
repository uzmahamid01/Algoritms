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


#sorting column wise: sort each column of a matrix in ascending order
#Approach:
# /*
# 1. traverse through the matrix
# 2. find the transpose of the matrix
# 3. store the transpose in new Matrix
# 4. travers the rows of the Matrix[new one]
# 5. sort each row of the matrix using sort function
# 6. store the transpose of new into old Matrix
# 7. print the matrix

# ideal way:
# create three funtions 
# one for transpose 
# one for RowSort
# one for colSort
# then the main function
# */

print("------------------------------------------------")
def transpose(matrix, rows, cols):
    # Create a new matrix with transposed dimensions
    new_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Transpose the matrix
    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = matrix[i][j]
    
    return new_matrix

def sort_rows(matrix):
    # Sort each row of the matrix
    for row in matrix:
        row.sort()
    return matrix

def sort_columns(matrix, rows, cols):
    # Transpose the matrix, sort the rows (which are the original columns), and then transpose back
    transposed_matrix = transpose(matrix, rows, cols)
    sorted_transposed_matrix = sort_rows(transposed_matrix)
    sorted_matrix = transpose(sorted_transposed_matrix, cols, rows)
    
    # Print the sorted matrix
    for row in sorted_matrix:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    # Input matrix
    matrix = [
        [1, 6, 10],
        [8, 5, 9],
        [9, 4, 15],
        [7, 3, 60]
    ]
    
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Sort the matrix by columns
    sort_columns(matrix, rows, cols)


N = 4
#adjoint and inverse of matrix
def adjoinT(A):
    N = len(A)
    # adj = [[0 for _ in range(N)] for _ in range(N)]
    adj = [[0 for _ in range(N)] for _ in range(N)]
    # print("")
    # print("copied adjoint: ", adj )


    #Base Case
    if(len(A) == 1):
        adj[0][0] = 1
        return

    sign = 1
    temp = []

    temp = [[0 for _ in range(N)] for _ in range(N)]

    #print("temp = ", temp)


    for i in range(N):
        for j in range(N):
            x = getCofactor(A, temp, i, j, N)
            #print(x)

            sign = (-1) ** (i + j)

            adj[i][j] = (sign) *(determinant(temp, N-1))

    return adj
  

def getCofactor(A, temp, p, q, n):
    i =0
    j=0
    for row in range(n):
        for col in range(n):
            if (row != p and col != q):
                temp[i][j] = A[row][col]
                j+=1

                if (j ==  n-1):
                    j = 0
                    i += 1


def determinant(A, N):
    
    D = 0

    if (N == 1):
        return A[0][0]

    temp = []
    for i in range(N):
        temp.append([None for _ in range(N)])

    sign = 1

    for f in range(N):
        getCofactor(A, temp, 0, f, N)

        D += sign * A[0][f]* determinant(temp,N-1)


        sign = - sign 

    return D


def inverse(A):

    det = determinant(A, N)
    if (det == 0):
        return False

    adj = adjoinT(A)
    inv = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            inv[i][j] = adj[i][j]/ det

    return inv





A = [[5, -2, 2, 7], [1, 0, 0, 3], [-3, 1, 5, 0], [3, -1, -9, 4]]
Adj = adjoinT(A)

# Calculate the determinant of A
det = determinant(A, len(A))

# Print the adjoint and determinant of matrix A
print("Adjoint of the matrix:")
for row in Adj:
    print(row)
    print("")
print(f"Determinant of the matrix: {det}")
print("")
inv_A = inverse(A)

# Print the inverse of matrix A
if inv_A:
    print("Inverse of the matrix:")
    for row in inv_A:
        print(row)
else:
    print("Inverse of the matrix does not exist.")