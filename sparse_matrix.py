# This class to creat a sparse matrix, and do numerous operations on them.
class Sparse_Matrix:
    def __init__(self, rows, cols, *args):
        '''Takes in 2 integer values to create an object with a desired number of rows and columns as 0 values,
        values in the certain coordanites can be specified with additional arguments, [row, column, value].'''
            
        assert type(rows) is int and rows > 0, 'Sparse_Matrix.__init__:rows('+str(rows)+') is not an integer greater than 0'  
        assert type(cols) is int and cols > 0, 'Sparse_Matrix.__init__:rows('+str(cols)+') is not an integer greater than 0'
        
        if len(args) > 0:
            for ro, co, va in args:
                assert type(ro) is int and ro > -1 and ro < rows, 'Sparse_Matrix.__init__:row at('+ str((ro,co,va)) +') is not an integer greater or equal to 0 or rows.'
                assert type(co) is int and co > -1 and co < cols, 'Sparse_Matrix.__init__:col at('+ str((ro,co,va)) +') is not an integer greater or equal to 0 or cols.'
                assert type(va) is (int or float) and va % 1 == 0, 'Sparse_Matrix.__init__:val at('+ str((ro,co,va)) +') is not a numeric integer or float.'                                                      
        self.rows = rows
        self.cols = cols
        self.matrix = dict()
        if len(args) > 0:
            for coor in args:
                if coor[2] == 0:
                    pass
                else:
                    if (coor[0], coor[1]) in self.matrix.keys():
                        raise AssertionError('Sparse_Matrix.__init__: repeated index '+ str((coor[0], coor[1])) + '.')
                    self.matrix[(coor[0], coor[1])] = coor[2]
    
    def __str__(self):
        '''Printable object'''
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'

    def size(self):
        '''Returns the size of the matrix, (#rows, #columns)'''
        return (self.rows, self.cols)

    def __len__(self):
        '''Returns the number of values in the matrix rows * columns'''
        return self.rows * self.cols

    def __bool__(self):
        '''Returns False if matrix is empty, else True'''
        return False if len(self.matrix) == 0 else True
    
    def __repr__(self):
        '''Returns the representation of the matrix'''
        return 'Sparse_Matrix(' + str(self.rows) + ', ' + str(self.cols) + ', ' +  ', '.join('('+(','.join(str(k[0]) + str(k[1]) + str(v)))+')' for k, v in self.matrix.items()) + ')'

    def __getitem__(self, arg):
        '''Return a value from the matrix'''
        if (type(arg) is not tuple) or (len(arg) != 2) or (self.rows <= arg[0]) or (arg[0] < 0) or (self.cols <= arg[1]) or (arg[1] < 0):
            raise TypeError('Sparse_Matrix.__getitem__: row or col at '+ str(arg) + ' is not valid.')
        for item in arg:
            if type(item) is not int:
                raise TypeError('Sparse_Matrix.__getitem__: row or col at '+ str(arg) + ' is not valid.')
        return self.matrix.get(arg, 0)
    
    def __setitem__(self, arg, value):
        '''Set a value in the matrix'''
        if type(value) is not (int or float) or value % 1 != 0: 
            raise TypeError('Sparse_Matrix.__setitem__: value at '+ str(value) + ' is not a numeric integer or float.')
        if type(arg) is not tuple or len(arg) != 2 or self.rows <= arg[0] or arg[0] < 0 or self.cols <= arg[1] or arg[1] < 0:
            raise TypeError('Sparse_Matrix.__setitem__: row or col at '+ str(arg) + ' is not valid.')
        for item in arg:
            if type(item) is not int:
                raise TypeError('Sparse_Matrix.__getitem__: row or col at '+ str(arg) + ' is not valid.')
        if value == 0:
            if arg in self.matrix:
                del self.matrix[arg]
            else:
                pass
        else:
            self.matrix[arg] = value
            
    def __delitem__(self, arg):
        '''Delete a value from the matrix, making it 0'''
        if type(arg) is not tuple or len(arg) != 2 or self.rows <= arg[0] or arg[0] < 0 or self.cols <= arg[1] or arg[1] < 0:
            raise TypeError('Sparse_Matrix.__delitem__: row or col at '+ str(arg) + ' is not valid.')
        if arg in self.matrix:
            del self.matrix[arg]

    def row(self, row):
        '''Return a row from the matrix'''
        assert type(row) is int and row > -1 and row < self.rows, 'Sparse_Matrix.row:row at('+ str(row) +') is not an integer greater or equal to 0 or rows.'
        rows = list()
        for i in range(self.cols):
            if (row, i) in self.matrix.keys():
                rows.append(self.matrix[(row, i)])
            else:
                rows.append(0)
        return tuple(rows)
    
    def col(self, col):
        '''Return a col from the matrix'''
        assert type(col) is int and col > -1 and col < self.cols, 'Sparse_Matrix.col:row at('+ str(col) +') is not an integer greater or equal to 0 or rows.'
        cols = list()
        for i in range(self.rows):
            if (i, col) in self.matrix.keys():
                cols.append(self.matrix[(i, col)])
            else:
                cols.append(0)
        return tuple(cols)
    
    def details(self):
        '''Somewhat details about the matrix; size, coordinates that are not 0s, and all rows in a tuple'''
        return str(self.rows) + 'x' + str(self.cols) + ' -> ' + str(self.matrix) + ' -> ' + str(tuple([Sparse_Matrix.row(self, i) for i in range(self.rows)]))

    def __call__(self, rows, cols):
        '''Change the matrix into a desired size, shrink or expand'''
        assert type(rows) is int and rows > 0, 'Sparse_Matrix.__init__:rows('+str(rows)+') is not an integer greater than 0'  
        assert type(cols) is int and rows > 0, 'Sparse_Matrix.__init__:rows('+str(rows)+') is not an integer greater than 0'
        new_matrix = {k: v for k, v in self.matrix.items()}
        new_matrix_dummy = {k: v for k, v in self.matrix.items()}
        for k, v in new_matrix.items():
            if k[0] >= rows or k[1] >= cols:
                del new_matrix_dummy[k]
        self.__dict__['rows'] = rows  
        self.__dict__['cols'] = cols        
        self.__dict__['matrix'] = new_matrix_dummy       
        return Sparse_Matrix(rows, cols, *[(k[0], k[1], v) for k, v in new_matrix_dummy.items()])
        
    def __iter__(self):
        '''Iterate over the coordinates and their values which are not 0s'''
        return iter([(k[0], k[1], v) for k, v in sorted(self.matrix.items(), key = lambda x: x[1])])
    
    def __neg__(self): 
        '''Multiply all the values by negative 1 and return a new matrix'''
        return Sparse_Matrix(self.rows, self.cols, *[(k[0], k[1], -v) for k, v in self.matrix.items()])
        
    def __pos__(self):
        '''Multiply all the values by 1 and return a new matrix'''
        return Sparse_Matrix(self.rows, self.cols, *[(k[0], k[1], v) for k, v in self.matrix.items()])
        
    def __abs__(self):
        '''Change all the values with their absolute values and return a new matrix'''
        return Sparse_Matrix(self.rows, self.cols, *[(k[0], k[1], abs(v)) for k, v in self.matrix.items()])
    
    def __add__(self, arg):
        '''Add 2 matrices together and return a new matrix'''
        if type(arg) != Sparse_Matrix or type(self) != Sparse_Matrix:
            if not type(arg) is (int or float): raise TypeError('Sparse_Matrix.__radd__:arg at('+ str(arg) +') is not a numeric integer or float or Sparse_Matrix.')  
        new_matrix = {k: v for k, v in self.matrix.items()}
        if type(arg) == Sparse_Matrix:   
            if Sparse_Matrix.__len__(self) != Sparse_Matrix.__len__(arg):
                raise AssertionError ('Sparse_Matrix.__radd__:arg at('+ str(arg) +') is not the same size.')
            for k, v in arg.matrix.items():
                if k in new_matrix:
                    new_matrix[k] += v 
                else:
                    new_matrix[k] = v
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    if (i, j) in self.matrix:
                        new_matrix[(i, j)] += arg
                    else:
                        new_matrix[(i, j)] = arg
        return Sparse_Matrix(self.rows, self.cols, *[(k[0], k[1], v) for k, v in new_matrix.items()])
    
    def __radd__(self, arg):
        '''Add 2 matrices together and return a new matrix'''
        return Sparse_Matrix.__add__(self, arg)
    
    def __sub__(self, arg):
        '''Substract 2 matrices together and return a new matrix'''
        if type(arg) == int or (type(arg) == float and arg % 1 == 0):
            return Sparse_Matrix.__add__(self, -arg)
        elif type(arg) == Sparse_Matrix:
            return Sparse_Matrix.__add__(self, Sparse_Matrix.__neg__(arg))
        else:
            raise TypeError('Sparse_Matrix.__rsub__:arg at('+ str(arg) +') is not an int, float or Sparse_Matrix.')
        
    def __rsub__(self, arg):
        '''Substract 2 matrices together and return a new matrix'''
        if type(arg) == int or (type(arg) == float and arg % 1 == 0):
            return Sparse_Matrix.__add__(Sparse_Matrix.__neg__(self), arg)
        elif type(arg) == Sparse_Matrix:
            return Sparse_Matrix.__add__(self, Sparse_Matrix.__neg__(arg))
        else:
            raise TypeError('Sparse_Matrix.__rsub__:arg at('+ str(arg) +') is not an int, float or Sparse_Matrix.')
        
    def __mul__(self, arg):
        '''Multiply 2 matrices with normal matrix rules'''
        if type(arg) == Sparse_Matrix:
            assert self.rows == arg.cols, 'Sparse_Matrix.__mul__:arg at('+ str(arg) +') does not have same number of cols in its rows.'
            new_matrix = list()
            for i in range(self.rows):
                for j in range(arg.cols):
                    new_matrix.append((i, j, sum([self.row(i)[a] * arg.col(j)[a] for a in range(self.cols)])))
            return Sparse_Matrix(self.rows, arg.cols, *[item for item in new_matrix if item[2] != 0])
        elif type(arg) == (int or float):
            if arg == 0:
                return Sparse_Matrix(self.rows, self.cols)
            else:
                return Sparse_Matrix(self.rows, self.cols, *[(k[0], k[1], v*arg) for k, v in self.matrix.items()])
        else:
            raise TypeError('Sparse_Matrix.__mul__:arg at('+ str(arg) +') is not an int, float or Sparse_Matrix.')
            
    def __rmul__(self, arg):
        '''Multiply 2 matrices with normal matrix rules'''
        return Sparse_Matrix.__mul__(self, arg)
    
    def __pow__(self, arg):
        '''Return the power of the matrix'''
        assert self.rows == self.cols, 'Sparse_Matrix.__pow__:arg at('+ str(arg) +') does not have same number of cols in its rows or arg is not an int.'
        if not (type(arg) is int or float) : raise TypeError('Sparse_Matrix.__pow__:arg at('+ str(arg) +') is not a numeric integer or float or Sparse_Matrix.')  
        if not arg > 0 : raise AssertionError('Sparse_Matrix.__pow__:arg at('+ str(arg) +') is not a numeric integer or float or Sparse_Matrix.')  
        new_matrix = Sparse_Matrix(self.rows, self.cols, *[(k[0], k[1], 1) for k, _ in self.matrix.items()])
        for _ in range(arg):
            new_matrix = Sparse_Matrix.__mul__(new_matrix, self)
        return new_matrix
        
    def __eq__(self, arg):
        '''Compare 2 matrices'''
        if type(arg) == Sparse_Matrix and Sparse_Matrix.size(self) == Sparse_Matrix.size(arg):
            for i in range(self.rows):
                if self.row(i) != arg.row(i):
                    return False
            return True
        elif type(arg) == int and len(self.matrix.keys()) == Sparse_Matrix.__len__(self):
            for _, v in self.matrix.items():
                if v != arg:
                    return False
            return True
        elif arg == 0 and len(self.matrix.keys()) == 0:
            return True
        else:
            return False
            
    def __setattr__(self, name, value):
        '''Dangeroues: Be careful, set attributes in the class.'''
        if (name not in ['rows', 'cols', 'matrix']) or name in self.__dict__:
            raise AssertionError
        else:
            self.__dict__[name] = value

