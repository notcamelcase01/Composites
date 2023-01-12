import numpy as np
from Get2DMatrix import Get2DMatrixFormOf4thOrderTensor

c = Get2DMatrixFormOf4thOrderTensor(np.random.rand(3,3,3,3))
print(c)
