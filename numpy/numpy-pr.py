# How is list diff from numpy?
# List ---> Slow
#          Homogeneous
#          Takes more memory

# Numpy ---> Fast
#          Heterogeneous
#          Takes less memory

# Why is numpy faster?
# Numpy uses fixed type of values (same values throughout the whole array). (Heterogeneous)
# Faster to read less bytes of memory
# Check the image1.png

# Applications of numpy
# Mathematics, Plotting, Backend(Pandas, connect4, Digital Photography),Machine Learning, 


import numpy as np

a = np.array([1,2,3])
print(a)
print(type(a))

b = np.array([4,5,6])
print(b)
print(a+b)

print("#################2D arrays###############")

c = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(c)
print(type(c))

# Get the dimension of the array :
print(a.ndim) # 1
print(c.ndim) # 2

# Get the shape of the array : 
print(a.shape) # (3,) --> 1 row and 3 columns
print(c.shape) # (2, 3) --> 2 rows and 3 columns

# Get the size of array (Total numbers of elements in the array) :
print(a.size) # 3
print(c.size) # 6

# Get the type of array (type of data stored in the array) :
print(a.dtype) # int64
print(c.dtype) # float64

# Get the size of the item :
print(a.itemsize) # 8 --> int64 (64 bits)
print(c.itemsize) # 8 --> float64 (64 bits)

# Get the total memory occupied by the array in bytes :
print(a.nbytes) # 24 --> 3 * 8
print(c.nbytes) # 48 --> 6 * 8

