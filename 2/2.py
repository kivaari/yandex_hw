import numpy as np


def calculate(products, cook):
    n, m, k = cook[0], cook[1], cook[2]
    milk , eggs, powder = 0, 0, 0
    
    print("Молоко, литры:", round(milk, 1))
    print("Яйца, штуки:", round(eggs, 1))
    print("Мука, кг:", round(powder, 1))

products = np.array([
    [0.1, 2, 0.05],
    [0.2, 1, 0.2],
    [0.5, 3, 0.3]])

cook = [10, 32, 8]
# print(products[0][2])
calculate(products, cook)