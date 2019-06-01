# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

# this solution has a space complexity of O(n2)
def zeroMatrix(matrix):  # this functions seraches for zeros in the matrix and updates the new matrix with zeros

    for row in range(len(matrix)):
        for col in range(len(matrix)):

            if matrix[row][col] == 0:
                convertToZeroMatrix(matrix, row, col)
    return copy

def convertToZeroMatrix(matrix, row, col):  #for the each colunm and row make zeros
    for i in range(len(matrix[row])):
        copy[row][i] = 0
    for j in range(len(matrix)):
        copy[j][col] = 0

if __name__ == '__main__':

    matrix = [[1,1,1],
              [0,1,1],
              [1,1,1]]

    copy = [row[:] for row in matrix]
    print(zeroMatrix(matrix))




# my solution with O(n) space complexity solution
def zeroMatrix(matrix):

    firstColumn = False
    firstRow = False

#check if an element in the first row or column is zero
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            firstColumn = True

    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            firstRow = True

#check inner matrix to know if any cell is equal to 0.
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  #if so make first element in the row equal to 0
                matrix[0][j] = 0  #if so make first element in the col equal to 0


#check if the first row has zero, if so make all the element in the row equal to zero
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

#check if the first col has zero, if so make all the element in the col equal to zero
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(len(matrix)):
                matrix[i][j] = 0
#now if the element in the first row is zero make every element in the first column zero
    if firstRow:
        for j in range(0,len(matrix[0])):
            matrix[0][j] = 0
#Also if all the element in the first column is zero make every element in the first row zero
    if firstColumn:
        for i in range(0,len(matrix)):
            matrix[i][0] = 0
            
    return matrix
if __name__ == '__main__':

    matrix = [[1,1,1],
              [0,1,1],
              [1,1,1]]

    copy = [row[:] for row in matrix]
    print(zeroMatrix(matrix))
