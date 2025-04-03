import numpy as np
import matplotlib.pyplot as plt

# Conjunto de datos de edades
edades = [23, 30, 35, 40, 45, 50, 55]

# Cálculos estadísticos
media = np.mean(edades)
mediana = np.median(edades)
varianza = np.var(edades)
desviacion_estandar = np.std(edades)

# Mostrar resultados
print(f"Media: {media:.2f} años")
print(f"Mediana: {mediana:.2f} años")
print(f"Varianza: {varianza:.2f} años²")
print(f"Desviación estándar: {desviacion_estandar:.2f} años")

# Gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(range(len(edades)), edades, color='skyblue', label='Edades individuales')
plt.axhline(media, color='red', linestyle='--', label=f'Media ({media:.2f} años)')
plt.axhline(mediana, color='green', linestyle=':', label=f'Mediana ({mediana:.2f} años)')

# Líneas para mostrar la desviación estándar
plt.axhline(media + desviacion_estandar, color='gray', linestyle='-.', alpha=0.5, label='±1 desviación estándar')
plt.axhline(media - desviacion_estandar, color='gray', linestyle='-.', alpha=0.5)

# Personalizar gráfico
plt.title('Distribución de Edades y Estadísticos', pad=20)
plt.xlabel('Personas (índice)')
plt.ylabel('Edad (años)')
plt.xticks(range(len(edades)), labels=[f"Persona {i+1}" for i in range(len(edades))])
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()