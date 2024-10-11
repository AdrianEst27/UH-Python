import pandas as pd

#Cargas los datos
ventas_df = pd.read_csv("productos.csv")

# Mostrar las primer 5 filas.
print(ventas_df.head())

# Mostrar las últimas filas
print(ventas_df.tail(3))

# Obtener información de las columnas y sus tipos
print(ventas_df.info())

# Calcular estadísticas descriptivas
media_cantidad = ventas_df['Cantidad'].mean()
mediana_cantidad = ventas_df['Cantidad'].median()
desviacion_cantidad = ventas_df['Cantidad'].std()

# Imprimir estadísticas
print(f" > Media de cantidad: {media_cantidad}")
print(f" > Mediana de cantidad: {mediana_cantidad}")
print(f" > Desviación de cantidad: {desviacion_cantidad}")

# Calcular el precio total de cada venta (cantidad * precio) y agregarlo como una nueva columna.
ventas_df['Total'] = ventas_df['Cantidad'] * ventas_df['Precio']
print(ventas_df.head(5))

# Crear un nuevo dataframe que contenga solo las ventas del producto.
uvas_df = ventas_df[ventas_df['Producto'] == 'Uvas']
print(uvas_df.head(5))

# Ordenar el dataframe original por la columna "Total" en orden descendente
ventas_df_ordenado = ventas_df.sort_values(by = 'Total', ascending = False)
print(ventas_df_ordenado.head())