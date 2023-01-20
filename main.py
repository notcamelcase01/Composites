import numpy as np
from GetNDMatrix import Get2DMatrixFormOf4thOrderTensor  , Get2DIdentity , kdelta , Get4DIdentity
c = Get2DMatrixFormOf4thOrderTensor(Get4DIdentity())
b = np.zeros((3,3,3,3))
b[0][0][0][0] = 23
b[1][1][1][1] = 12
b[2][2][2][2] = 10
b[1][2][1][2] = 112
b[0][2][0][2] = 15
b[0][1][0][1] = 21
b[0][0][1][1] = 213
b[1][1][0][0] = 213
b[0][0][2][2] = 9
b[2][2][0][0] = 9
b[1][1][2][2] = 1
b[2][2][1][1] = 1



print(Get2DMatrixFormOf4thOrderTensor(b,True))
