import numpy as np


def snake(m, n):
    matrix = np.zeros((m, n), dtype=int)
    count = 1

    for i in range(m):
        if i % 2 == 0:
            matrix[i] = np.arange(count, count + n)
        else:
            matrix[i] = np.arange(count + n - 1, count - 1, -1)
        count += n
    return matrix

print(snake(3, 4))