import numpy as np


def to_tableau(c, a, b):
    xb = [eq + [x] for eq, x in zip(a, b)]
    z = c + [0]
    return np.array(xb + [z])
