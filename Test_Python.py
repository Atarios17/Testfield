import numpy as np
import pandas as pd

w = np.arange(0,78,2)
v = w**2

def f(x,y):
    x = x**2
    y = sqrt(y)
    return x+y

z = f(w,v) + 2137
