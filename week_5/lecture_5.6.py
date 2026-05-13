
def initialize_mat(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):

        C[i].append(0)
    return C    
print(initialize_mat(3))


def dot_product(u,v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans = ans + (u[i]*v[i])
    return ans

print(dot_product([2,3,5],[2,2,2]))


def row(M,i):
    dim=len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l    
A =[2,3,2],[3,3,3],[4,5,3]
print(row(A,2))


def column(M,j):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[k][j])
    return l
B =[2,5,2],[3,3,3],[4,5,3]
print(column(B,1))

def mat_mul(J,K):
    dim = len(J)
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            # C[i][j] = ith row of A * jth col of B
            C[i][j] = dot_product(row(A,i),column(B,j))
    return C
A =[[2,3,2],[3,3,3],[4,5,3]]
B =[[2,5,2],[3,3,3],[4,5,3]]
print(mat_mul(A,B))

