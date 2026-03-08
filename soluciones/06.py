import pandas as pd
import re

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Limpiar ciudad
df['ciudad'] = df['ciudad'].astype(str)
df['ciudad'] = df['ciudad'].str.replace(r'[^a-zA-Z ]', '', regex=True)
df['ciudad'] = df['ciudad'].str.strip().str.title()

# Contar Bogota
cantidad = df[df['ciudad'] == 'Bogota'].shape[0]

print(f"La ciudad Bogota aparece: {cantidad} registros después de limpiar")