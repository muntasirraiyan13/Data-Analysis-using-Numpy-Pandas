import numpy as np
A=np.array([
    [1,2,3],
    [4,5,6]
])

B=np.array([
    [7,8],
    [9,10],
    [11,12]
])
dot_product=np.dot(A,B)
print(dot_product)

C=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(C)
trace_of_C=np.trace(C)
print(trace_of_C)

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
det_of_matrix=np.linalg.det(matrix)
print(det_of_matrix)

rank_matrix=np.linalg.matrix_rank(matrix)
print(rank_matrix)





