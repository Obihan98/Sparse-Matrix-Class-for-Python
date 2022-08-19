# Sparse-Matrix-Class-for-Python
Sparse Matrix Class created for Python

Here is the sample run for the class!
```
>>> from sparse_matrix import Sparse_Matrix

>>> x = Sparse_Matrix(5, 5, [0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1])

>>> repr(x)
'Sparse_Matrix(5, 5, (0,0,1), (1,1,1), (2,2,1), (3,3,1))'

>>> print(x)
5x5:[1  0  0  0  0
     0  1  0  0  0
     0  0  1  0  0
     0  0  0  1  0
     0  0  0  0  0]
     
>>> x.size()
(5, 5)

>>> len(x)
25

>>> bool(x)
True

>>> x[1, 1]
1

>>> x[1, 0]
0

>>> x[1, 0] = 10
>>> x[1, 0]
10
>>> print(x)
5x5:[ 1   0   0   0   0
     10   1   0   0   0
      0   0   1   0   0
      0   0   0   1   0
      0   0   0   0   0]
      
>>> del x[1, 0]
>>> print(x)
5x5:[1  0  0  0  0
     0  1  0  0  0
     0  0  1  0  0
     0  0  0  1  0
     0  0  0  0  0]
     
>>> x.row(2)
(0, 0, 1, 0, 0)

>>> x.details()
'5x5 -> {(0, 0): 1, (1, 1): 1, (2, 2): 1, (3, 3): 1} -> ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 0))'

>>> print(x)
5x5:[1  0  0  0  0
     0  1  0  0  0
     0  0  1  0  0
     0  0  0  1  0
     0  0  0  0  0]
     
>>> x(3, 3)
Sparse_Matrix(3, 3, (0,0,1), (1,1,1), (2,2,1))
>>> print(x)
3x3:[1  0  0
     0  1  0
     0  0  1]
     
>>> for row in x: print(row)
...
(0, 0, 1)
(1, 1, 1)
(2, 2, 1)

>>> print(-x)
3x3:[-1   0   0
      0  -1   0
      0   0  -1]
      
>>> x = -x
>>> print(x)
3x3:[-1   0   0
      0  -1   0
      0   0  -1]
      
>>> print(abs(x))
3x3:[1  0  0
     0  1  0
     0  0  1]
     
>>> print(x+x)
3x3:[-2   0   0
      0  -2   0
      0   0  -2]
      
>>> x += x
>>> print(x)
3x3:[-2   0   0
      0  -2   0
      0   0  -2]
      
>>> print(x*10)
3x3:[-20    0    0
       0  -20    0
       0    0  -20]
       
>>> print(x**3)
3x3:[-8   0   0
      0  -8   0
      0   0  -8]
      
>>> print(x != x)
False
```
