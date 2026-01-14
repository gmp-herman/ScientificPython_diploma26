import wrapmodule
from wrapmodule import MatrixOp as mp

rows = 2
columns = 2
matrix1=mp(rows,columns)
matrix2=mp(rows,columns)
print(matrix1)

print("Addition:")
print("Addition: ", matrix1+matrix2)

print("Multiplication:")
print(matrix1*matrix2)

print("Inverse:")
print(matrix1.inverse())

print("Determinant:")
print(matrix1.determinant())

print("Eigenvalues:")
print(matrix1.eigenvalues())