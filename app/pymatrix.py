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

    return [[A[row][col] + B[row][col] for col in range(size[1])] for row in range(size[0])]


def identity_matrix(rows: int, columns: int):
    """
    Create an identity matrix with given size
    """
    return [[1 if row == col else 0 for col in range(columns)] for row in range(rows)]


def scalar_multiplication(A: list, c: float) -> list:
    """
    Scalar multiplication of A
    """
    size = size_of(matrix=A)
    return [[A[row][col] * c for col in range(size[1])] for row in range(size[0])]


def matrix_product(A: list, B: list) -> list:
    """
    Matrix product of A x B

    A(nxm) => a[i][j]
    B(mxp) => b[i][j]

    Raise:
    - ValueError: Number of columns of A must equal to number of rows of B.

    returns
      C(nxp) = A[i] * B[j]
    """
    size_a = size_of(matrix=A)
    size_b = size_of(matrix=B)

    if size_a[1] != size_b[0]:
        raise ValueError(
            'Number of columns of A must equal to number of rows of B')

    return [[sum(A[i][x] * B[x][j] for x in range(size_a[1]))
             for j in range(size_b[1])] for i in range(size_a[0])]
