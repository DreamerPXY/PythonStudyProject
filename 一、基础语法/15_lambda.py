func1 = lambda a,b:a+b
print(func1(1,2))

func2 = lambda *args : len(args)
print(func2(2,3,4))

import time
time.sleep(1)

time = 1

import numpy as np


a = np.random.normal(0,1,(8,10))
print(type(a))
var = a > 1
print(var)
a[a>1] = 2
print(a)
