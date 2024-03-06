"""
Concatenate:
Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:

import numpy
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])
print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]
If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.

import numpy
array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])
print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]    

Task:
You are given two integer arrays of size N x P and M x P (N&M are rows and P is the column).
Your task is to concatenate the arrays along axis

Input Format

The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format:
Print the concatenated array of size (N + M) x P.

"""
import numpy

n, m, p = map(int, input().split())

#numpy.array is the command to create and array
arrayN = numpy.array([input().strip().split() for x in range(n)], dtype=int)
arrayM = numpy.array([input().strip().split() for y in range(m)], dtype=int)
print(numpy.concatenate((arrayN, arrayM), axis=0))