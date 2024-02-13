import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Загрузка датасета
data = pd.read_csv('penguins.csv')

# Удаление пустых строк
data = data.dropna()

# Копирование столбцов species, bill_length_mm, bill_depth_mm
labels = data['species']
features = data[['bill_length_mm', 'bill_depth_mm']]

# Разбиение на обучающую и тестовую выборку
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.2, random_state=123)

best_accuracy = 0
worst_accuracy = 1

# Обучение 20 моделей KNN
for n_neighbors in range(1, 11):
    for weights in ['uniform', 'distance']:
        knn = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights)
        knn.fit(train_features, train_labels)
        predictions = knn.predict(test_features)
        accuracy = accuracy_score(test_labels, predictions)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = knn
        if accuracy < worst_accuracy:
            worst_accuracy = accuracy
            worst_model = knn

# Вывод результатов
print('Best accuracy: {:.6f}'.format(best_accuracy))
print('Worst accuracy: {:.6f}'.format(worst_accuracy))
