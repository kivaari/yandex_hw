import numpy as np

def scalar(a, b):
    scalar_product = round(sum(a[i] * b[i] for i in range(len(a))), 1)
    return scalar_product

def euclid(x, y):
    euc = round(np.sqrt(sum((x[i] - y[i])**2 for i in range(len(x)))), 2)
    return euc

def manhatt(z, v):
    manhattan_distance = sum(np.abs(z[i] - v[i]) for i in range(len(z)))
    return manhattan_distance

def matrix_x_vec(vec, matrix):
    m, n = matrix.shape
    n_vec = len(vec)
    if n != n_vec:
        print("Количество столбцов матрицы не совпадает с длиной вектора, матрица транспонирована")
        transposed_m = np.transpose(matrix)
        result = np.dot(transposed_m, vec)
    else:
        result = np.dot(matrix, vec)
    return result

def determinant(matrix):
    transposed_m = np.transpose(matrix)
    determinant = np.linalg.det(transposed_m)
    return determinant

def last(x, y):
    result_matrix = np.dot(x, y)
    sum_of_elements = np.sum(result_matrix)
    unique, counts = np.unique(result_matrix, return_counts=True)
    most_common_element = unique[np.argmax(counts)]
    return sum_of_elements, most_common_element

def main():
    a = np.array([0.7, 1.9, 4, 3.2, 5.1, 2.7, 4.8])
    b = np.array([21, 40, 29, 31, 18, 31, 26])

    x = np.array([4, 7, 2, 1, 6, 1, 3, 3, 2, 8])
    y = np.array([2, 3, 8, 8, 8, 8, 7, 1, 0, 5])

    z = np.array([4, 7, 2, 1, 6, 1, 3, 3, 2, 8])
    v = np.array([2, 3, 8, 8, 8, 8, 7, 1, 0, 5])

    vec = np.array([0, 1, 4, 6])
    matrix = np.array([[3, 0, 0], [1, 0, 4], [5, 6, 4], [3, 3, 6]])

    m = np.array([[3, -1, 0], [2, 1, -1], [1, 5, 4]])

    m1 = np.array([[1, 2, 6, 3], [1, 1, 4, 3], [-3, 4, -3, -3]])
    m2 = np.array([[1, 5], [1, 3], [6, 0], [-2, 4]])

    print("Скалярное произведение:", scalar(a, b))
    print("----------------------------------------------------------------------")
    print("Евклидово расстояние:", euclid(x, y))
    print("----------------------------------------------------------------------")
    print("Манхеттенское расстояние:", manhatt(z, v))
    print("----------------------------------------------------------------------")
    print("Произведение матрицы на вектор:", matrix_x_vec(vec, matrix))
    print("----------------------------------------------------------------------")
    print("Определитель матрицы после транспонирования:", determinant(m))
    print("----------------------------------------------------------------------")
    print("Сумма всех элементов матрицы и число встречающееся чаще всего в производной матрице:", last(m1, m2))

if __name__ == "__main__":
    main()