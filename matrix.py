from decimal import *
from collections import Iterable

'''
Matrix class can be used to do matrix operations
'''
class Matrix:
    '''
    Internal class for representing rows in matrix
    '''
    class MVector:
        def __init__(self, *values):
            if len(values) == 1 and isinstance(values[0], Iterable):
                values = values[0]
            self._data = [Decimal(v) for v in values]

        def __getitem__(self, indices):
            return self._data[indices]

        def __setitem__(self, indices, values):
            if isinstance(values, Iterable):
                self._data[indices] = [Decimal(v) for v in values]
            else:
                self._data[indices] = Decimal(values)

        def __str__(self):
            string = "["
            for i in range(len(self)-1):
                string += "{0}, ".format(self[i])
            string += "{0}]".format(self[len(self)-1])

            return string

        def __len__(self):
            return len(self._data)

    def __init__(self, rows, columns):
        if columns < 1 or rows < 1:
            raise ValueError("Matrix dimensions must be greater than zero")

        self._data = [Matrix.MVector([0 for x in range(columns)]) for y in range(rows)]

    def __str__(self):
        string=""
        for i in range(self.columnCount() * 7 + 3):
            string += "_"
        string += "\n"

        # i = Zeile, j = spalte
        for i in range(self.rowCount()):
            string += "| "
            for j in range(self.columnCount()):
                string += "{0:^7.3}".format(self[i][j])
            string += "|\n"

        for i in range(self.columnCount() * 7 + 3):
            string += "-"

        return string

    def __repr__(self):
        return self.__str__()

    '''
    Returns a new matrix C.
    self * other = C
    '''
    def __mul__(self, other):
        if self.columnCount() != other.rowCount():
            raise ValueError("Cannot multiply those matrices since dimensions are incompatible")

        c = Matrix(self.rowCount(), other.columnCount())
        for i in range(c.rowCount()):
            for j in range(c.columnCount()):
                # Calculate sum from line and column
                value = 0
                row = self[i]
                column = other.columnAt(j)
                for k in range(len(row)):
                    value += row[k] * column[k]

                c[i][j] = value

        return c

    def __pow__(self, pot):
        if pot == 0:
            identity = Matrix(self.columnCount(), self.columnCount())
            for i in range(identity.rowCount()):
                identity[i][i] = 1

            return identity

        # Use binary exponentiation to enhance speed
        bits = ("{0:b}".format(pot))[1:]
        result = self
        for bit in bits:
            if bit == "0":
                result = result * result
            else:
                result = result * result
                result = result * self

        return result

    def __getitem__(self, indices):
        return self._data[indices]

    def __setitem__(self, indices, value):
        if isinstance(value, Iterable):
            if not len(value) == self.columnCount():
                raise ValueError("Can not change matrix length")
            value = [Decimal(v) for v in value]
        else:
            value = [Decimal(value) for i in range(self.columnCount())]

        self._data[indices] = value

    def __eq__(self, other):
        if other.rowCount() != self.rowCount() or other.columnCount() != self.columnCount():
            return False

        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                if other[i][j] != self[i][j]:
                    return False

        return True

    def __ne__(self, other):
        return not (other == self)

    def isSymmetrical(self):
        return self.transpose() == self

    def rowAt(self, index):
        return self[index]

    def columnAt(self, index):
        return Matrix.MVector([row[index] for row in self])

    def transpose(self):
        transposed = Matrix(self.rowCount(), self.columnCount())
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                transposed[j][i] = self[i][j]

        return transposed

    def rowCount(self):
        return len(self._data)

    def columnCount(self):
        return len(self[0])
