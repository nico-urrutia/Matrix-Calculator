from fractions import Fraction
def transpose_m(matrix: list[list])->list[list]:
    trasp: list[list] = []
    for i in range(len(matrix[0])):
        row_transp: list = []
        for row in matrix:
            row_transp.append(row[i])
        trasp.append(row_transp)
    return trasp

def mult_diagonal(matrix):
    mult: int = 1
    for i in range(len(matrix)):
        mult*=Fraction(matrix[i][i])
    return mult

def partial_pivot(matrix, index):
    for j in range(index, len(matrix)): # If the pivot element is 0, we look for another row to swap with.
        if matrix[j][j]!=0:
            matrix[index], matrix[j] = matrix[j], matrix[index]
            break
    return matrix

def clean_matrix(matrix):
    nueva_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(str(Fraction(element))) #Fraction module used to make the matrix more readable
        nueva_matrix.append(new_row)
    return nueva_matrix

def substract_rows(row1, row2, mult):
    for i in range(len(row1)):
        row1[i]=row1[i]-(row2[i]*mult)

def turn_triangular(matrix): 
    sign: int = 1
    for i in range(len(matrix)-1):
        pivot = matrix[i][i]
        if pivot == 0:
            matrix = partial_pivot(matrix, i)
            sign*=-1
            pivot = matrix[i][i]
            if pivot == 0: #If the pivot can't be changed, return 0.
                return [[0]]
        for j in range(i+1, len(matrix)):
            substract_rows(matrix[j], matrix[i], Fraction(matrix[j][i], pivot))#With Fraction i avoid losing accuracy with decimal digits.
    matrix[0][0]*=sign
    return matrix

def get_minor(matrix, col, row):
    minor1 = []
    for i in range(0, len(matrix)):
        if i != row:
            minor1.append(matrix[i])
    trasp_minor = transpose_m(minor1)
    trasp_minor.remove(trasp_minor[col])
    return transpose_m(trasp_minor)

def determinante_matrix(matrix: list[list])->int:
    determinante: int = 0
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        for i in range(len(matrix)):
            determinante+=pow(-1, i)*matrix[0][i]*determinante_matrix(get_minor(matrix, i, 0))
        return determinante

def adjunta(matrix):
    mat_adjunta = []
    for i in range(len(matrix)):
        row_adj = []
        for j in range(len(matrix)):
            sign=pow(-1, i+j)
            row_adj.append(determinante_matrix(get_minor(matrix, j, i))*sign)
        mat_adjunta.append(row_adj)
    return transpose_m(mat_adjunta)

def gauss_mat_range(matrix):
    matrix_triangular = turn_triangular(matrix)
    mat_range = 0
    for row in matrix_triangular:
        null: bool = True
        for element in row:
            if Fraction(element)!=0:
                null = False
        if not null:
            mat_range+=1
    return mat_range
 
def identity_matrix(matrix):
    identity:  list = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(0)
        identity.append(row)
    for k in range(len(matrix)):
        identity[k][k]+=1
    return identity

def augment_matrix(matrix):
    identity = identity_matrix(matrix)
    augmented = []
    for i in range(len(matrix)):
        row = []
        for number in matrix[i]:
            row.append(number)
        for number in identity[i]:
            row.append(number)
        augmented.append(row)
    return augmented

def get_inverse_from_aug(matrix):
    inverse = []
    for i in range(len(matrix)):
        fila = []
        for j in range(len(matrix), len(matrix[0])):
            fila.append(matrix[i][j])
        inverse.append(fila)
    return inverse

def inverse_gauss_jordan(matrix):
    if determinante_matrix(matrix) == 0:
        raise ValueError("The matrix is not invertible (determinant = 0).")
    if len(matrix)!=len(matrix[0]):
        raise ValueError("The matrix is not invertible (not square).")
    augmented_matrix = augment_matrix(matrix)
    for i in range(len(matrix)):
        pivot = augmented_matrix[i][i]
        if pivot == 0:
            partial_pivot(augmented_matrix, i)
        for j in range(i, len(augmented_matrix[i])):
            augmented_matrix[i][j] = Fraction(augmented_matrix[i][j],pivot)
        for k in range(len(augmented_matrix)):
            if k == i:
                continue
            substract_rows(augmented_matrix[k], augmented_matrix[i], augmented_matrix[k][i])
    inverse = get_inverse_from_aug(augmented_matrix)
    return clean_matrix(inverse)

def system_gauss_jordan(matrix, results):#Note that it takes TWO arguments: the matrix and the results vector. This might cause problems with user input and parsing(have to fix that later).
    pass  # Placeholder for future implementation

class Matrix:
    def __init__(self, data: list[list]):
        self.data = data

    def transpose_m(self):
        return Matrix(clean_matrix(transpose_m(self.data)))

    def determinante_rec(self):
        return determinante_matrix(self.data)
    
    def determinante_tri(self):
        triangular = turn_triangular(self.data)
        return mult_diagonal(triangular)

    def rank_gauss(self):
        return gauss_mat_range(self.data)
    
    def inverse_gauss_jordan(self):
        inv = inverse_gauss_jordan(self.data)
        return Matrix(clean_matrix(inv))

C2 = [
    [3, 2, 8, 4],
    [5, 6, 5, 8],
    [9, 10, 1, 2],
    [1, 4, 3, 6]
    ]