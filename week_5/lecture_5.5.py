A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[6,2,3],[4,2,1]]



C = [[0,0,0],[0,0,0],[0,0,0]]


dim = 3

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j]=C[i][j] + A[i][k] * B[k][j]

print(C)














