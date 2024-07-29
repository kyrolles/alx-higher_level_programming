def square_matrix_simple(matrix=[]):
    new1_matrix = list(map(lambda x: x * x, matrix[0]))
    new2_matrix = list(map(lambda x: x * x, matrix[1]))
    new3_matrix = list(map(lambda x: x * x, matrix[2]))
    new_matrix = [new1_matrix, new2_matrix, new3_matrix]
    return new_matrix
