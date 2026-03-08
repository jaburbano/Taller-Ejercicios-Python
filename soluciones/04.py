import pandas as pd
import codecs

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Descifrar nombres
df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Limpiar nombres
df['nombre'] = df['nombre'].str.strip().str.title()

# Contar nombres
conteo = df['nombre'].value_counts()

nombre_mas_frecuente = conteo.idxmax()
cantidad = conteo.max()

print(f"El nombre más frecuente es: {nombre_mas_frecuente} y aparece {cantidad} veces")