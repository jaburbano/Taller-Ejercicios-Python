import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Limpiar ciudad
df['ciudad'] = df['ciudad'].astype(str)
df['ciudad'] = df['ciudad'].str.replace(r'[^a-zA-Z ]', '', regex=True)
df['ciudad'] = df['ciudad'].str.strip().str.title()

# Contar ciudades únicas
cantidad = df['ciudad'].nunique()

print(f"Cantidad de ciudades únicas después de limpiar: {cantidad}")