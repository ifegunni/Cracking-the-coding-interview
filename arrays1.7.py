# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

#This solution is my O(n2) solution

def rotate(matrix):

    newMatrix = [row[:] for row in matrix] #we have to copy the matrix so we don't edit the original
    a = len(matrix)
    for i in range(a):  #traverse through each row and column
        for j in range(a):
            newMatrix[i][j] = matrix[a-j-1][i] # swap clockwise 90 degrees
    return newMatrix

if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(matrix)
    print(rotate(matrix))




# Rotating a matrix 180 degrees clockwise

from copy import deepcopy   # using deepcopy to copy matrix into new matrix

def rotate(matrix):
    oneEightyMatrix = deepcopy(matrix)
    n = len(matrix)
    for i in range(n):  # algorithm
        for j in range(n):
            oneEightyMatrix[i][j] = matrix[n-i-1][n-j-1]
    return oneEightyMatrix

if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(matrix)
    print(rotate(matrix))
    
    
    
#In place solution with O(n2) time complexity and O(1) space complexity
def rotate(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix[j][i]
    return matrix

if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(matrix)
    print(rotate(matrix))
    
    
    
    
#In place solution with O(n2) time complexity and O(1) space complexity
def rotate(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i): #only change
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # also changed
    return matrix

if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(matrix)
    print(rotate(matrix))
