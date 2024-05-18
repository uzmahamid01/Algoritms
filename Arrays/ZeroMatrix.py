def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    zero_row = set()
    zero_col = set()
 
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    for i in zero_row:
        for j in range(n):
            matrix[i][j] = 0
    
    for i in zero_col:
        for j in range(m):
            matrix[i][j] = 0

            

    return matrix

def main():
    matrix = [
        [1, 2, 3],
        [4, 9, 6],
        [7, 8, 0]
    ]
    
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    rotated = zero_matrix(matrix)
    
    print("\nZero matrix:")
    for row in rotated:
        print(row)

main()