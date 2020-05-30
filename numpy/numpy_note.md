# Numpy Notes
## Quick Start
This is summarized from [Numpy Quick Start](https://numpy.org/devdocs/user/quickstart.html).

Before we start , we may have the question: why numpy? The similar data structure is List.
The following items are summarized from [the geeksforgeeks article](https://www.geeksforgeeks.org/python-lists-vs-numpy-arrays/).
* **List**: A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.
           * The list can be homogeneous or heterogeneous.
           * Element wise operation is not possible on the list
           * Python list is by default 1 dimensional. But we can create an N-Dimensional list. But then too it will be 1 D list storing another 1D list
           * Elements of a list need not be contiguous in memory.
* **Numpy**: 
          * Array are by default Homogeneous, which means data inside an array must be of the same Datatype. 
          * Element wise operation is possible
          * Numpy array has the various function, methods, and variables, to ease our task of matrix computation.
          * Elements of an array are stored contiguously in memory.
* Advantages of using Numpy Arrays Over Python Lists:
          * consumes less memory.
          * fast as compared to the python List.
          * convenient to use.

```python
import numpy as np
l = [1,2,3]
np.array(l)
```
```
array([1, 2, 3, 4])
```
```python 
l = [1,2,3,4]
l+1
```
![image.png](../files/numpy_error1.png)
```python
l = [1,2,3,4]
np.array(l) + 1
```
```
array([2, 3, 4, 5])
```
```python 
l = ['a',1,2,3]
np.array(l)
```
```
array(['a', '1', '2', '3'], dtype='<U1')
```
## Create Numpy 
Create numpy from List. 
```python
a=np.array([1,2,3,4])
print(a)
print(a.ndim)
print(a.shape)
```
```
[1 2 3 4]
1
(4,)
```
Multi-dimension array:
```python
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.shape)
print(a.ndim)
```
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
(3, 3)
2
```
Functions to create special np array.
```python
a=np.arange(10)
print(a)
b=np.arange(1,100,20)
print(b)
print(np.linspace(0, 1, 6))
print(np.ones((3, 3)))
print(np.zeros((2, 2)))
print(np.eye(3))
```
```
[0 1 2 3 4 5 6 7 8 9]
[ 1 21 41 61 81]
[0.  0.2 0.4 0.6 0.8 1. ]
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
[[0. 0.]
 [0. 0.]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```
We can also create the diag matrix by 
```python
np.diag(np.array([1, 2, 3, 4]))
```
Create numpy array from **np.random**:
```python
np.random.rand(3,4)
```
to create shape=(3,4) array.


## Numpy Index
This is summarized from [the index of numpy page](https://numpy.org/doc/stable/user/basics.indexing.html).
Single element indexing:
```python
a = np.array([1,2,3])
print(a[0])
print(a[-1])
```
continuous indexing:
```python 
x = np.arange(10)
print('x[2:5] is',x[2:5])
print('x[:-7] is', x[:-7])
```
```
x[2:5] is [2 3 4]
x[:-7] is [0 1 2]
```
**:-7** means goes back to start.
```python
y = np.arange(35).reshape(5,7)
print('y is:', y)
y[1:5:2,::3]
```
```
y is: [[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]]
array([[ 7, 10, 13],
       [21, 24, 27]])
```
**1:5:2** means start to end by step 2. **::3** means 0 to end by step size 3.

Arbitray indexing:
```python
x = np.arange(10,1,-1)
x[np.array([3, 3, 1, 8])]
```
Please figure out the answer yourself.

Note that, slicing for the multi-dimensional array is similar to the 1-d array.

Boolean or “mask” index arrays:
```python 
x = np.arange(30).reshape(2,3,5)
print(x)
b = np.array([[True, True, False], [False, True, True]])
print(b)
x[b]
```
```
[[[ 0  1  2  3  4]
  [ 5  6  7  8  9]
  [10 11 12 13 14]]

 [[15 16 17 18 19]
  [20 21 22 23 24]
  [25 26 27 28 29]]]
[[ True  True False]
 [False  True  True]]
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29]])
```
