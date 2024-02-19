import numpy as np
import math


def calculate(products, cook):
    n, m, k = cook[0], cook[1], cook[2]
    milk = products[0][0] * n + products[1][0] * m + products[2][0] * k
    eggs = products[0][1] * n + products[1][1] * m + products[2][1] * k
    powder = products[0][2] * n + products[1][2] * m + products[2][2] * k
    print("Молоко, литры:", math.ceil(milk))
    print("Яйца, штуки:", math.ceil(eggs))
    print("Мука, кг:", math.ceil(powder))


products = np.array([
    [0.1, 2, 0.05],
    [0.2, 1, 0.2],
    [0.5, 3, 0.3]])

cook = [10, 32, 8]
# print(products[0][2])
calculate(products, cook)
