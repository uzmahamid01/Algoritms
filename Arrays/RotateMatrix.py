def rotate_matrix(matrix):
    n = len(matrix)
    # print(n)
    
    # Create a new matrix for the rotated result
    rotated_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]
    
    return rotated_matrix


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    rotated = rotate_matrix(matrix)
    
    print("\nRotated matrix by 90 degrees:")
    for row in rotated:
        print(row)

main()
