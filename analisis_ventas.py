import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {
    'Producto': ['A', 'B', 'C', 'D'],
    'Ventas': [100, 150, 200, 120]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("Datos de ventas:")
print(df)

# Crear un gráfico de barras
df.plot(kind='bar', x='Producto', y='Ventas', title='Ventas por producto')

# Mostrar el gráfico
plt.show()
