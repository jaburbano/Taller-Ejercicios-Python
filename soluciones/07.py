import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Limpiar ciudad
df['ciudad'] = df['ciudad'].astype(str)
df['ciudad'] = df['ciudad'].str.replace(r'[^a-zA-Z ]', '', regex=True)
df['ciudad'] = df['ciudad'].str.strip().str.title()

# Contar Medellin
cantidad = df[df['ciudad'] == 'Medellin'].shape[0]

print(f"La ciudad Medellin aparece: {cantidad} registros después de limpiar")