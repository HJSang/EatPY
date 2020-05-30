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
l = ['a',1,2,3]
np.array(l)
```
```
array(['a', '1', '2', '3'], dtype='<U1')
```
