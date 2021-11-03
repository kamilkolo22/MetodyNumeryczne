def upper_matrix(A):
    A = A.astype(float)
    for k in range(len(A)-1):
        for i in range(k,len(A)-1):
            w = A[i+1][k] / A[k][k]
            print(A)
            for j in range(k, len(A)):
                A[i+1][j] = A[i+1][j] - A[k][j]*w
    return A
