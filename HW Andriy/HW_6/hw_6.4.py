import random
matrix_1 = [[random.randint(10, 99) for x in range(5)] for y in range(5)]
matrix_2 = [[random.randint(10, 99) for x in range(5)] for y in range(5)]

def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print matrix[i][j],
        print
    print

def matrix_max(matrix):
    test = matrix[0][0]
    test_coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if test < matrix[i][j]:
                test = matrix[i][j]
                test_coordinates = [i, j]
    return test_coordinates

print "Original matrix 1:"
matrix_print(matrix_1)

print "Original matrix 2:"
matrix_print(matrix_2)

matrix_1_x = matrix_max(matrix_1)[0]
matrix_1_y = matrix_max(matrix_1)[1]
matrix_2_x = matrix_max(matrix_2)[0]
matrix_2_y = matrix_max(matrix_2)[1]

print "The largest element in Matrix 1 is {} with coordinates {} \nand the largest element in Matrix 2 is {} with " \
      "coordinates {}\n".format(matrix_1[matrix_1_x][matrix_1_y], matrix_max(matrix_1),\
                                matrix_2[matrix_2_x][matrix_2_y],matrix_max(matrix_2))

matrix_1[matrix_1_x][matrix_1_y], matrix_2[matrix_2_x][matrix_2_y] \
    = matrix_2[matrix_2_x][matrix_2_y], matrix_1[matrix_1_x][matrix_1_y]

print "New matrix 1:"
matrix_print(matrix_1)

print "New matrix 2:"
matrix_print(matrix_2)