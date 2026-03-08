import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Limpiar profesión
df['profesion'] = df['profesion'].astype(str)
df['profesion'] = df['profesion'].str.replace(r'[^a-zA-Z ]', '', regex=True)
df['profesion'] = df['profesion'].str.strip().str.title()

# Contar profesiones únicas
cantidad = df['profesion'].nunique()

print(f"La cantidad de profesiones únicas después de limpiar es: {cantidad}")