# Sparse-Matrix-Class-for-Python
Sparse Matrix Class created for Python

Here is the sample run for the class!

# Creating the object
• Called with number of rows and columns, and value specfied coordinates
```
>>> x = Sparse_Matrix(5, 5, [0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1])
>>> print(x)
5x5:[1  0  0  0  0
     0  1  0  0  0
     0  0  1  0  0
     0  0  0  1  0
     0  0  0  0  0]
```

• Can be called without a specified coordinates  
```
>>> x = Sparse_Matrix(5, 5)
>>> print(x)
5x5:[0  0  0  0  0
     0  0  0  0  0
     0  0  0  0  0
     0  0  0  0  0
     0  0  0  0  0]
```

# Methods

• `object.size()` -> a method that returns a tuple with number of rows and columns
```
>>> x.size()
(5, 5)
```

• `object.row()` -> a method that returns the specified row
```
>>> x.row(2)
(0, 0, 1, 0, 0)
```

• `object.details()` -> a method that returns some details about the matrix
```
>>> x.details()
'5x5 -> {(0, 0): 1, (1, 1): 1, (2, 2): 1, (3, 3): 1} -> ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 0))'
```

# Overloaded Operators

• `len(object)` -> returns the number of rows multiplied by the number of columns
```
>>> len(x)
25
```

• `repr(object)` -> representation of the class object
```
>>> repr(x)
'Sparse_Matrix(5, 5, (0,0,1), (1,1,1), (2,2,1), (3,3,1))'
```

• `bool(object)` = True when at least one values is not 0
```
5x5:[0  0  0  0  0
     0  3  0  0  0
     0  0  0  0  0
     0  0  0  0  0
     0  0  0  0  0]
>>> bool(x)
True
```

• `bool(object)` = False when all values in the matrix are 0s
```
5x5:[0  0  0  0  0
     0  0  0  0  0
     0  0  0  0  0
     0  0  0  0  0
     0  0  0  0  0]
>>> bool(x)
False
```

• `object.__getitem__(1, 1) / object[1, 1]` -> returns the specified value
```
>>> x[1, 1]
1
>>> x[1, 0]
0
```

• `object.__setitem__(1, 1) / object[1, 1] = 1` -> changes the value in a specified coordinate
```
>>> x[1, 0] = 10
>>> x[1, 0]
10
```

• `object.__delitem__(1, 1) / del object[1, 1]` -> changes the value in a specified coordinate to 0
```
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
```
     
• `object.__call__(3, 3) / object(3, 3)` -> changes the matrix into a desired size, shrink or expand
```
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
```

• `object.__iter__()` -> Itirate over the values from top left corner to bottom right corner, from top to bottom by only showing non 0 values
```
>>> for row in x: print(row)
(0, 0, 1)
(1, 1, 1)
(2, 2, 1)
```

• `object.__neg__() / -object` -> Negate all the values
```
>>> print(x)
3x3:[-1   0   0
      0  -1   0
      0   0  -1]
```

• `object.__abs__() / abs(object)` -> Absolute values of all the values
```
>>> print(abs(x))
3x3:[1  0  0
     0  1  0
     0  0  1]
```

• `object.__add__() / object_1 + object_2` -> addition
```
>>> print(x)
3x3:[-1   0   0
      0  -1   0
      0   0  -1]
>>> print(x + x)
3x3:[-2   0   0
      0  -2   0
      0   0  -2]
```

• `object.__radd__() / object_1 += object_2` -> addition
```
>>> print(x)
3x3:[-1   0   0
      0  -1   0
      0   0  -1]      
>>> x += x
>>> print(x)
3x3:[-2   0   0
      0  -2   0
      0   0  -2]
```

• `object.__mul__() / object_1 ** object_2` -> multiplication
```
>>> print(x)
3x3:[-2   0   0
      0  -2   0
      0   0  -2]
>>> print(x*10)
3x3:[-20    0    0
       0  -20    0
       0    0  -20]
```

• `object.__pow__() / object_1 ** object_2` -> power
```
>>> print(x)
3x3:[-2   0   0
      0  -2   0
      0   0  -2]
>>> print(x**3)
3x3:[-8   0   0
      0  -8   0
      0   0  -8]
```

• `object.__eq__() / object_1 != or == object_2` -> equality
```
>>> print(x)
3x3:[-2   0   0
      0  -2   0
      0   0  -2]
>>> print(x != x)
False
```
