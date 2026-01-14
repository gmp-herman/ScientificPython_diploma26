import numpy as np
class MatrixOp:
    """Matrix operations"""

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix1 = self._create_matrix(n, m)
        self.matrix2 = self._create_matrix(n, m)

    def _create_matrix(self, n, m):
        num = 1
        matrix = [[num + j + i*m for j in range(m)] for i in range(n)]
        return matrix

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Matrices must have the same dimensions")

        result = MatrixOp(self.n, self.m)

        result.matrix1 = [[self.matrix1[i][j] + other.matrix1[i][j] for j in range(self.m)] for i in range(self.n)]

        result.matrix2 = [[ self.matrix2[i][j] + other.matrix2[i][j] for j in range(self.m)] for i in range(self.n)]

        return result

    def __str__(self):
        return (f"Matrix 1:\n{self._format(self.matrix1)}\n\n" f"Matrix 2:\n{self._format(self.matrix2)}")

    def _format(self, matrix):
        return "\n".join(str(row) for row in matrix)

    def __mul__(self, other):

        result = MatrixOp(self.n, other.m)

        result.matrix1 = [[ sum(self.matrix1[i][k] * other.matrix1[k][j] for k in range(self.m)) for j in range(other.m)] for i in range(self.n)]  

        result.matrix2 = [[ sum(self.matrix2[i][k] * other.matrix2[k][j] for k in range(self.m)) for j in range(other.m)] for i in range(self.n)]
    
        return result

    def inverse(self):

        mat = np.array(self.matrix1)
        return np.linalg.inv(mat)

    def determinant(self):

        mat = np.array(self.matrix1)
        return np.linalg.det(mat)

    def eigenvalues(self):

        mat = np.array(self.matrix1)
        return np.linalg.eigvals(mat)
