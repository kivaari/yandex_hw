import numpy as np


def mean_squared_error(y_true, y_pred):
    return np.mean((np.array(y_true) - np.array(y_pred))**2)


def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(np.array(y_true) - np.array(y_pred)))


def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


y = [float(x) for x in input().split()]
y_pred = [float(x) for x in input().split()]

mse = round(mean_squared_error(y, y_pred), 2)
mae = round(mean_absolute_error(y, y_pred), 2)
rmse = round(root_mean_squared_error(y, y_pred), 2)

print("MSE: {:.2f}".format(mse))
print("MAE: {:.2f}".format(mae))
print("RMSE: {:.2f}".format(rmse))