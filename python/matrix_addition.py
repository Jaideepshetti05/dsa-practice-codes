def matrix_addition(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

if __name__ == "__main__":
    X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    for r in matrix_addition(X, Y):
        print(r)
