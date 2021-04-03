
import numpy as np
import matplotlib.pyplot as plt

def gallery(array, ncols=3):
    nindex, height, width
    nrows = nindex//ncols
    assert nindex == nrows*ncols
    # want result.shape = (height*nrows, width*ncols, intensity)
    result = (array.reshape(nrows, ncols, height, width)
              .swapaxes(1,2)
              .reshape(height*nrows, width*ncols, intensity))
    return result



