"""
PyMatrix contains some of the matrix operations using in linear algebra
"""


def size_of(matrix: list) -> tuple:
    """
    Returns the size of the matrix

    returns:
        (#rows, #cols)
    """
    return len(matrix), len(matrix[0])


def sum_of(A: list, B: list):
    """
    Sum of matrix

    A(nxm) => a[i][j]
    B(nxm) => b[i][j]

    Raise:
    - ValueError: Most have the same size.

    returns
      C(nxm) = a[i][j] + b[i][j]
    """
    size = size_of(matrix=A)

    if size != size_of(matrix=B):
        raise ValueError('Must have the same size')

    result = []

    for row in range(size[0]):
        row_result = []
        for col in range(size[1]):
            row_result.append(A[row][col] + B[row][col])

        result.append(row_result)

    return result


def identity_matrix(rows: int, columns: int):
    """
    Create an identity matrix with given size
    """
    result = []
    for row in range(rows):
        row_result = []
        for column in range(columns):
            row_result.append(1 if row == column else 0)
        result.append(row_result)
    return result
