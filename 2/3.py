import pandas as pd
import numpy as np


def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


def k_neighbours(n, k, matrix):
    distances = []
    query_point = matrix[n]

    for i, point in enumerate(matrix):
        if i != n:
            distance = euclidean_distance(query_point, point)
            distances.append((i, distance))

    distances.sort(key=lambda x: x[1])

    return distances[:k]


def main():
    n = int(input())
    k = int(input())
    df = pd.read_csv('penguins.csv')
    df = df.dropna()
    matrix = df[['bill_length_mm', 'bill_depth_mm']]
    matrix_array = matrix.values
    neighbours = k_neighbours(n, k, matrix_array)
    for neighbour in neighbours:
        print(matrix_array[neighbour[0]])


if __name__ == "__main__":
    main()
