import numpy as np

def kdelta(i,j):
    return int(i == j)

def GetIndex(i,j):
    flag = (10*i+j) == 21 or (10*i+j) == 20 or (10*i+j) == 10
    if(i == j):
        a = i
    else:
        a = 6 - j - i + 3*flag
    return a,flag

def Get2DMatrixFormOf4thOrderTensor(C, isSymmetric = False):
    C_1 = np.zeros((9,9))
    for i in range(3):
        for j in range(3):
            a, f1 = GetIndex(i, j)
            for k in range(3):
                for l in range(3):
                    b,f2 = GetIndex(k,l)
                    if not isSymmetric:
                        C_1[a][b] = 0.25*(C[i][j][k][l] + (-1)**(f1)*C[j][i][k][l] + (-1)**(f2)*C[i][j][l][k] + (-1)**(f2)*(-1)**(f1)*C[j][i][l][k])
                    else:
                        C_1[a][b] = C[i][j][k][l]
    return C_1[:6,:6] if(isSymmetric)  else C_1

def Get2DIdentity(n = 3):
    return np.eye(n)

def Get4DIdentity(n = 3):
    I = np.zeros((n,n,n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    I[i][j][k][l] = kdelta(i,j)*kdelta(k,l)
    return I

def GetOrthrotropic(E1 , E2 , E3 , v12 , v21 , v31 , v13 , v32 , v23 , G23 , G31 , G12, stiffness = True):
    C = np.zeros((6,6))
    C[0][0] = 1/E1
    C[0][2] = -v12/E2
    C[0][2] = -v13/E3
    C[2][0] = -v21/E1
    C[2][2] = 1/E2
    C[2][2] = -v23/E3
    C[2][0] = -v31/E1
    C[2][2] = -v32/E2
    C[2][2] = 1/E3
    C[4][4] = 1/G23
    C[5][5] = 1/G31
    C[6][6] = 1/G12
    if stiffness:
        return C
    return np.linalg.inv(C)
