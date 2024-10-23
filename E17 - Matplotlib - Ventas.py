import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame
data = {
    'Ciudad': ['Acapulco', 'Acapulco', 'Acapulco', 'Monterrey', 'Monterrey', 'Monterrey', 'Guadalajara', 'Guadalajara', 'Guadalajara'],
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo'],
    'Temperatura': [25, 28, 30, 15, 18, 22, 18, 20, 25]
}
df = pd.DataFrame(data)

# Calcular la temperatura media por ciudad
temp_media = df.groupby('Ciudad')['Temperatura'].mean()
print(temp_media)

# Función lambda para convertir Celsius a Fahrenheit
celsius_a_fahrenheit = lambda x: (x * 9/5) + 32

# Aplicar la función y crear una nueva columna
df['Temperatura_Fahrenheit'] = df['Temperatura'].apply(celsius_a_fahrenheit)

# Función para graficar la temperatura de una ciudad
def graficar_temperatura(df, ciudad, titulo='Temperatura Mensual', color='blue'):
    df_ciudad = df[df['Ciudad'] == ciudad]
    plt.plot(df_ciudad['Mes'], df_ciudad['Temperatura'], color=color)
    plt.title(titulo)
    plt.xlabel('Mes')
    plt.ylabel('Temperatura (°C)')
    plt.show()

# Ejemplo de uso de la función
graficar_temperatura(df, 'Acapulco', titulo='Temperaturas en Acapulco', color='red')

# Gráfico de barras con temperaturas medias
plt.bar(temp_media.index, temp_media)
plt.title('Temperatura Media por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Temperatura Media (°C)')
plt.show()

# Boxplot para comparar la distribución de temperaturas
plt.boxplot([df[df['Ciudad'] == ciudad]['Temperatura'] for ciudad in df['Ciudad'].unique()])
plt.xticks([1, 2, 3], df['Ciudad'].unique())
plt.title('Distribución de Temperaturas por Ciudad')
plt.ylabel('Temperatura (°C)')
plt.show()