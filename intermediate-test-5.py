# Write a program to perform matrix multiplication on two given matrices.

def matrix_multiplication(A, B):
    # Get the number of rows and columns for matrices A and B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Ensure that the number of columns in A is equal to the number of rows in B
    if cols_A != rows_B:
        return "Matrices cannot be multiplied due to incompatible dimensions."

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Example usage
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = matrix_multiplication(A, B)

if isinstance(result, str):
    print(result)
else:
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
