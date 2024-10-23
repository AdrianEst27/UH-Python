import pandas as pd
import matplotlib.pyplot as plt

# DataFrame
data = {
    'Día': [1, 1, 1, 2, 2, 2, 3, 3, 3, 30, 30, 30],
    'Catería': ['Camisas', 'Pantalones', 'Zapatos', 'Camisas', 'Pantalones', 'Zapatos',
                'Camisas', 'Pantalones', 'Zapatos','Camisas', 'Pantalones', 'Zapatos'],
    'Ventas': [25, 15, 10, 30, 20, 12, 28, 18, 8, 40, 35, 20]                
}
df = pd.DataFrame(data)

# Mostrar las primeras 5 filas
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Mostrar columnas y sus tipos
print(df.info())

# Función para calcular las ventas totales diarias
def VentasTotalesDiarias(df):
    vtd = df.groupby('Día')['Ventas'].sum()
    return vtd

# Impresión de resultados de la función VentasTotalesDiarias
print(VentasTotalesDiarias(df).to_markdown(numalign="left", stralign="left"))

# Función para obtener las ventas de una categoría específica
def VentasCategoria(df, categoria):
    vc = df[df['Categoria'] == categoria]
    return vc['Ventas']

