import numpy as np
from GetNDMatrix import Get2DMatrixFormOf4thOrderTensor  , Get2DIdentity , kdelta , Get4DIdentity
c = Get2DMatrixFormOf4thOrderTensor(Get4DIdentity(),True)
print(c)
