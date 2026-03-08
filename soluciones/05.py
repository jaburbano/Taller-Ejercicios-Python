import pandas as pd
import codecs

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Descifrar apellidos
df['apellido'] = df['apellido_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# Limpiar apellidos
df['apellido'] = df['apellido'].str.strip().str.title()

# Contar apellidos
conteo = df['apellido'].value_counts()

apellido_mas_frecuente = conteo.idxmax()
cantidad = conteo.max()

print(f"El apellido más frecuente es: {apellido_mas_frecuente} y aparece {cantidad} veces")