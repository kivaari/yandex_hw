import numpy as np


def r_squared(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    mean_y_true = np.mean(y_true)
    ss_total = np.sum((y_true - mean_y_true)**2)
    ss_res = np.sum((y_true - y_pred)**2)
    r2 = 1 - (ss_res / ss_total)
    return r2


y = [float(x) for x in input().split()]
y_pred = [float(x) for x in input().split()]

r_2 = round(r_squared(y, y_pred), 2)

print("R2: {:.2f}".format(r_2))