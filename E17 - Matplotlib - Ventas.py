import pandas as pd
import matplotlib.pyplot as plt

# Datos de temperatura por ciudad y mes
data = {
    'Ciudad': ['Acapulco', 'Acapulco', 'Acapulco', 'Monterrey', 'Monterrey', 'Monterrey', 'Guadalajara', 'Guadalajara', 'Guadalajara'],
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo'],
    'Temperatura': [25, 28, 30, 15, 18, 22, 18, 20, 25]
}
df = pd.DataFrame(data)

# Calcular la temperatura media por ciudad
temp_media = df.groupby('Ciudad')['Temperatura'].mean().round(2)
temp_media_df = temp_media.reset_index()
print("\nTemperatura media por ciudad:\n", temp_media_df)

# Convertir Celsius a Fahrenheit y agregar una nueva columna
df['Temperatura_Fahrenheit'] = df['Temperatura'].apply(lambda x: (x * 9/5) + 32)

# Función para graficar la temperatura mensual de una ciudad
def graficar_temperatura(df, ciudad, titulo='Temperatura Mensual', color='blue'):
    df_ciudad = df[df['Ciudad'] == ciudad]
    plt.figure()
    plt.plot(df_ciudad['Mes'], df_ciudad['Temperatura'], marker='o', color=color, label='Temperatura (°C)')
    plt.title(titulo)
    plt.xlabel('Mes')
    plt.ylabel('Temperatura')
    plt.legend()
    plt.grid(True)
    plt.show()

# Gráfica de temperaturas mensuales para Acapulco
graficar_temperatura(df, 'Acapulco', titulo='Temperaturas en Acapulco', color='red')

# Gráfico de barras con temperaturas medias
plt.figure()
plt.bar(temp_media.index, temp_media, color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Temperatura Media por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Temperatura Media (°C)')
plt.show()

# Boxplot para comparar la distribución de temperaturas por ciudad
plt.figure()
plt.boxplot([df[df['Ciudad'] == ciudad]['Temperatura'] for ciudad in df['Ciudad'].unique()])
plt.xticks([1, 2, 3], df['Ciudad'].unique())
plt.title('Distribución de Temperaturas por Ciudad')
plt.ylabel('Temperatura (°C)')
plt.show()
