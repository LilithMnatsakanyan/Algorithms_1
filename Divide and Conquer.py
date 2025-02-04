def matrix_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2 # divide and conquer
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    C11 = matrix_add(matrix_multiply(A11, B11), matrix_multiply(A12, B21))
    C12 = matrix_add(matrix_multiply(A11, B12), matrix_multiply(A12, B22))
    C21 = matrix_add(matrix_multiply(A21, B11), matrix_multiply(A22, B21))
    C22 = matrix_add(matrix_multiply(A21, B12), matrix_multiply(A22, B22))

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C

def matrix_add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

A = [[1, 2, 3, 4,1, 2, 3, 4],
    [9, 10, 11, 12,9, 10, 11, 12],
    [5, 6, 7, 8,5, 6, 7, 8],
    [5, 6, 7, 8,5, 6, 7, 8],
    [9, 10, 11, 12,9, 10, 11, 12],
    [12, 11, 10, 9,12, 11, 10, 9],
    [16, 15, 14, 13, 16, 15, 14, 13],
    [13, 14, 15, 16,13, 14, 15, 16]]

B = [[16, 15, 14, 13, 16, 15, 14, 13],
    [9, 10, 11, 12,9, 10, 11, 12],
    [16, 15, 14, 13, 16, 15, 14, 13],
    [5, 6, 7, 8,5, 6, 7, 8],
    [12, 11, 10, 9,12, 11, 10, 9],
    [8, 7, 6, 5, 8, 7, 6, 5],
    [12, 11, 10, 9,12, 11, 10, 9],
    [4, 3, 2, 1, 4, 3, 2, 1]]

C = matrix_multiply(A, B)
for row in C:
    print(row)
