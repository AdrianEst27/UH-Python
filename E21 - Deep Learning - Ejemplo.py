
# TODO: Práctica de Deep Learning
 
"""
    1. Cargar y Preparar Datos
    En ciencia de datos, solemos trabajar con datos en forma de tablas. Usaremos `pandas` para cargar y manipular datos. 
    Por ejemplo, carguemos el famoso conjunto de datos de iris:
"""

import pandas as pd
from sklearn.datasets import load_iris

# Cargar datos de ejemplo
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df.head()  # Mostrar las primeras filas

"""
    2. Explorar y Visualizar los Datos

    Con una exploración rápida, puedes identificar patrones, tendencias o problemas como datos faltantes. 
    `matplotlib` y `seaborn` son útiles para la visualización.
"""
import matplotlib.pyplot as plt
import seaborn as sns

# Histograma de las características
sns.pairplot(df, hue="target")
plt.show()

"""
    3. Preparación de los Datos

    Para un modelo efectivo, debes separar tus datos en características (variables independientes) y etiquetas (variable objetivo). 
    Luego, dividirlos en conjuntos de entrenamiento y prueba.
"""
from sklearn.model_selection import train_test_split

# Separar en características y etiquetas
X = df.drop(columns="target")  # Variables independientes
y = df["target"]               # Variable objetivo

# Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""
    4. Crear y Entrenar un Modelo

    Supongamos que queremos clasificar las especies de iris. 
    Usaremos el clasificador de vecinos más cercanos (K-Nearest Neighbors) como ejemplo:
"""
from sklearn.neighbors import KNeighborsClassifier

# Inicializar el modelo
model = KNeighborsClassifier(n_neighbors=3)

# Entrenar el modelo
model.fit(X_train, y_train)
 
"""
    5. Evaluar el Modelo

    Para evaluar qué tan bien funciona el modelo, puedes usar la exactitud, precisión, o cualquier métrica relevante.
"""
from sklearn.metrics import accuracy_score, classification_report

# Predecir en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitud: {accuracy}")
print(classification_report(y_test, y_pred))
 
"""
    6. Ajuste de Hiperparámetros

    Puedes optimizar el modelo ajustando los hiperparámetros, como el número de vecinos en KNN. 
    `GridSearchCV` ayuda a encontrar la mejor combinación:
"""
from sklearn.model_selection import GridSearchCV

# Definir el rango de hiperparámetros
param_grid = {'n_neighbors': [3, 5, 7, 9]}

# Inicializar la búsqueda en cuadrícula
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("Mejores parámetros:", grid_search.best_params_)

"""
    8. Guardar y Cargar el Modelo

    Para reutilizar el modelo en el futuro, puedes guardarlo con `joblib` o `pickle`:
"""
import joblib

# Guardar modelo
joblib.dump(model, "modelo_knn.pkl")

# Cargar modelo
loaded_model = joblib.load("modelo_knn.pkl")
