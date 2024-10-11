import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer el archivo CSV en un DataFrame
df = pd.read_csv("datos.csv")

# 2. Mostrar las primeras 5 filas
print("Primeras 5 filas:\n")
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# 3. Mostrar columnas y sus tipos
print("\nInformación de las columnas:\n")
print(df.info())

# 4. Calcular media, mediana y moda de la columna `Edad`
media_edad = df['Edad'].mean()
mediana_edad = df['Edad'].median()
moda_edad = df['Edad'].mode()

# 5. Imprimir los resultados
print(f"\nMedia de Edad: {media_edad}")
print(f"Mediana de Edad: {mediana_edad}")
print(f"Moda de Edad: {moda_edad[0]}") # Asumiendo que solo hay una moda

# 6. Crear un histograma de la columna `Edad`
plt.figure(figsize=(8, 5))
plt.hist(df['Edad'], bins=5, edgecolor='black')
plt.title('Histograma de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# 7. Crear un boxplot de la columna `Edad`
plt.figure(figsize=(6, 4))
plt.boxplot(df['Edad'])
plt.title('Boxplot de Edades')
plt.xlabel('Edad')
plt.show()