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

# a = np.array([1,2,3])
# print(a)
# print(type(a))

# b = np.array([4,5,6])
# print(b)
# print(a+b)

# print("#################2D arrays###############")

# c = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
# print(c)
# print(type(c))

# # Get the dimension of the array :
# print(a.ndim) # 1
# print(c.ndim) # 2

# # Get the shape of the array : 
# print(a.shape) # (3,) --> 1 row and 3 columns
# print(c.shape) # (2, 3) --> 2 rows and 3 columns

# # Get the size of array (Total numbers of elements in the array) :
# print(a.size) # 3
# print(c.size) # 6

# # Get the type of array (type of data stored in the array) :
# print(a.dtype) # int64
# print(c.dtype) # float64

# # Get the size of the item :
# print(a.itemsize) # 8 --> int64 (64 bits)
# print(c.itemsize) # 8 --> float64 (64 bits)

# # Get the total memory occupied by the array in bytes :
# print(a.nbytes) # 24 --> 3 * 8
# print(c.nbytes) # 48 --> 6 * 8

# print("Accessing/Changing Specific Elements, Rows, Columns, etc (slicing)")

# d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(d)

# # Get a specific element using r,c
# print(d[1,2]) # 7

# # Get a specific row : 
# print(d[0, :]) # [1 2 3 4]

# # Get a specific column : 
# print(d[:, 2]) # [ 3  7 11]

# # Slicing : d[row_slice, col_slice]
# print(d[0:3, 1:3]) # 

# # Slicing with steps : d[row_slice, col_slice, step_size]
# print(d[0:3:1, 1:3:2]) # 

# print("Fancy Slicing : ")
# print(d[0, 1:-1:2]) 

# # Changing elements : 
# d[2,3] = 100 # use the position to locate the element and assign it the value
# print(d)

# print("Column data changed : ") 
# d[:, 2] = 200 # use the position to locate the column and assign it the value
# print(d)


print("Initialize all sorts of Arrays : ")

# All 0s and 1s matrices

# 1x5 matrix with all 0s
print(np.zeros(5))

# 2x2 matrix with all 0s
print(np.zeros((2,2)))

# 3x2 matrix with all 0s
print(np.zeros((3,2)))

# All 1s matrix : 
print(np.ones((2,3)))

# All 1s matrix with specific data type : 
print(np.ones((2,3), dtype=int))
print(np.ones((2,3), dtype=float))


# Any other number matrix
print(np.full((3,3), 7))

# Use the shape of another array and but with diff values.float

# Ex : using the shape of e but with diff elements
e = np.array([[1,2,3,4], [5,6,7,8]])
print(e)

print(np.full_like(e, 22))


# Random decimal no.s
# gives you random decimal no.s. between 0 to 1 (both inclusive).
print(np.random.rand(4, 2, 3))
# 4 = Number of 2D blocks/matrices
# 2 = Number of rows in each block
# 3 = Number of columns in each block

# Random integer values : 
print(np.random.randint(100, size=(2,3)))
# Generates integers from 0 to 99 in a 2x3 grid.


# Identity Matrix : 
print(np.identity(5))
# Creates a 5x5 identity matrix (1s on the diagonal, 0s elsewhere).

arr = np.array([[1,2,3], [4,5,6]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

# 5 evenly spaced values
print(np.linspace(0,1,5))